#!/usr/bin/env python3
"""
LLM judgment probe for countability construction-sensitivity.

Dual measurement:
  1. Surprisal (primary): mean per-token negative log-prob. Deterministic.
  2. Likert rating (secondary): prompted 1-7 scale. 10 reps at temp=0.7.

Usage:
    python run_probe.py --model claude --measure surprisal
    python run_probe.py --model claude --measure likert --reps 10
    python run_probe.py --model claude --measure both --reps 10
"""

import csv
import re
import random
import argparse
import time
import math
from pathlib import Path
from datetime import datetime


# --- Prompts ---

SYSTEM_PROMPT_LIKERT = """You're participating in a linguistics study on sentence acceptability. You'll read a sentence and rate how natural it sounds on a 1-7 scale:

1 = Completely unacceptable
7 = Perfectly acceptable

Use the full range of the scale based on your intuitions as an English speaker. Give only the number."""


def build_likert_prompt(sentence):
    return f"Please rate this sentence:\n\n{sentence}\n\nRating (1-7):"


# --- Model backends ---

def surprisal_claude(sentence, model="claude-sonnet-4-6-20250514"):
    """Compute mean per-token surprisal via Anthropic API.

    Anthropic doesn't expose token log-probs directly.
    Fallback: use the prompted rating as the only measure for Claude,
    or use a proxy model that does expose log-probs.
    """
    # TODO: Anthropic API does not currently expose log-probs.
    # Options:
    #   1. Use prompted rating only for Claude
    #   2. Use a proxy (e.g., run sentence through a HuggingFace model)
    #   3. Wait for Anthropic to add log-prob support
    raise NotImplementedError(
        "Anthropic API does not expose token log-probs. "
        "Use --measure likert for Claude, or use a HuggingFace proxy."
    )


def surprisal_openai(sentence, model="gpt-4o"):
    """Compute mean per-token surprisal via OpenAI API."""
    from openai import OpenAI
    client = OpenAI()
    response = client.chat.completions.create(
        model=model,
        max_tokens=1,
        temperature=0,
        logprobs=True,
        messages=[
            {"role": "user", "content": f"Please repeat this sentence exactly:\n\n{sentence}"},
        ],
    )
    # Extract log-probs from the completion
    # Note: OpenAI returns log-probs for the completion tokens, not the prompt.
    # For surprisal of the sentence itself, we need the prompt log-probs,
    # which requires the completions (not chat) API or a different approach.
    # TODO: implement properly with the completions API or echo=True
    raise NotImplementedError(
        "Chat completions API doesn't return prompt token log-probs. "
        "Use the completions API or a HuggingFace model for surprisal."
    )


def surprisal_huggingface(sentence, model_name="meta-llama/Llama-3.1-8B"):
    """Compute mean per-token surprisal using a HuggingFace model.

    This is the most reliable method for surprisal measurement.
    Requires: pip install transformers torch
    """
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model.eval()

    inputs = tokenizer(sentence, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs, labels=inputs["input_ids"])
        # outputs.loss is mean cross-entropy over tokens
        mean_surprisal = outputs.loss.item() / math.log(2)  # convert nats to bits

    return mean_surprisal


def likert_claude(sentence, model="claude-sonnet-4-6-20250514"):
    """Get a 1-7 Likert rating from Claude."""
    from anthropic import Anthropic
    client = Anthropic()
    response = client.messages.create(
        model=model,
        max_tokens=5,
        temperature=0.7,
        system=SYSTEM_PROMPT_LIKERT,
        messages=[{"role": "user", "content": build_likert_prompt(sentence)}],
    )
    return response.content[0].text.strip()


def likert_openai(sentence, model="gpt-4o"):
    """Get a 1-7 Likert rating from GPT-4o."""
    from openai import OpenAI
    client = OpenAI()
    response = client.chat.completions.create(
        model=model,
        max_tokens=5,
        temperature=0.7,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT_LIKERT},
            {"role": "user", "content": build_likert_prompt(sentence)},
        ],
    )
    return response.choices[0].message.content.strip()


def likert_gemini(sentence, model="gemini-2.5-pro"):
    """Get a 1-7 Likert rating from Gemini."""
    import google.generativeai as genai
    m = genai.GenerativeModel(model, system_instruction=SYSTEM_PROMPT_LIKERT)
    config = genai.GenerationConfig(temperature=0.7, max_output_tokens=5)
    response = m.generate_content(build_likert_prompt(sentence), generation_config=config)
    return response.text.strip()


LIKERT_BACKENDS = {
    "claude": likert_claude,
    "gpt4o": likert_openai,
    "gemini": likert_gemini,
}


def parse_rating(text):
    """Extract a 1-7 integer from model response."""
    match = re.search(r'[1-7]', text)
    if match:
        return int(match.group())
    return None


# --- Main ---

def load_stimuli(path="stimuli.csv"):
    items = []
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append(row)
    return items


def run_surprisal(model_name="huggingface", output_dir="results"):
    """Run surprisal measurement (deterministic, one pass)."""
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)
    items = load_stimuli()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    outfile = output_dir / f"surprisal_{model_name}_{timestamp}.csv"

    with open(outfile, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "model", "item_id", "noun", "det", "construction",
            "item_type", "vp_set", "sentence", "surprisal_bits",
        ])
        writer.writeheader()

        for i, item in enumerate(items):
            print(f"  [{i+1}/{len(items)}] {item['item_id']}")
            try:
                surp = surprisal_huggingface(item["sentence"])
            except Exception as e:
                surp = None
                print(f"    ERROR: {e}")

            writer.writerow({
                "model": model_name,
                "item_id": item["item_id"],
                "noun": item["noun"],
                "det": item["det"],
                "construction": item["construction"],
                "item_type": item["item_type"],
                "vp_set": item["vp_set"],
                "sentence": item["sentence"],
                "surprisal_bits": surp,
            })

    print(f"Done. {len(items)} surprisal values written to {outfile}")
    return outfile


def run_likert(model_name, n_reps=10, seed=42, output_dir="results"):
    """Run Likert rating collection."""
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)

    query_fn = LIKERT_BACKENDS[model_name]
    items = load_stimuli()
    rng = random.Random(seed)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    outfile = output_dir / f"likert_{model_name}_{timestamp}.csv"

    total = len(items) * n_reps

    with open(outfile, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "rep", "model", "item_id", "noun", "det", "construction",
            "item_type", "vp_set", "sentence", "raw_response", "rating",
            "timestamp",
        ])
        writer.writeheader()

        for rep in range(1, n_reps + 1):
            rep_items = items.copy()
            rng.shuffle(rep_items)
            print(f"Rep {rep}/{n_reps}...")

            for item in rep_items:
                try:
                    raw = query_fn(item["sentence"])
                    rating = parse_rating(raw)
                except Exception as e:
                    raw = f"ERROR: {e}"
                    rating = None

                writer.writerow({
                    "rep": rep,
                    "model": model_name,
                    "item_id": item["item_id"],
                    "noun": item["noun"],
                    "det": item["det"],
                    "construction": item["construction"],
                    "item_type": item["item_type"],
                    "vp_set": item["vp_set"],
                    "sentence": item["sentence"],
                    "raw_response": raw,
                    "rating": rating,
                    "timestamp": datetime.now().isoformat(),
                })

                time.sleep(0.05)

    print(f"Done. {total} ratings written to {outfile}")
    return outfile


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run LLM judgment probe")
    parser.add_argument("--model", choices=["claude", "gpt4o", "gemini", "huggingface"],
                        default="claude")
    parser.add_argument("--measure", choices=["surprisal", "likert", "both"],
                        default="both")
    parser.add_argument("--reps", type=int, default=10,
                        help="Likert repetitions per item (ignored for surprisal)")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    if args.measure in ("surprisal", "both"):
        if args.model in ("claude", "gpt4o", "gemini"):
            print(f"NOTE: Surprisal not available via {args.model} API. Using HuggingFace.")
            run_surprisal("huggingface")
        else:
            run_surprisal(args.model)

    if args.measure in ("likert", "both"):
        if args.model == "huggingface":
            print("ERROR: Likert ratings require a chat model (claude/gpt4o/gemini).")
        else:
            run_likert(args.model, n_reps=args.reps, seed=args.seed)
