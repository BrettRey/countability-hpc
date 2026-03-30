#!/usr/bin/env python3
"""
LLM judgment probe for countability construction-sensitivity.

Adapted from Independent_relative_whose/scripts/simulate_experiment_llm.py

Runs each stimulus N times per model with temperature > 0 to capture
response variability. No personas — variance comes from the model itself.

Usage:
    python run_probe.py --model claude --reps 30
    python run_probe.py --model gpt4o --reps 30
    python run_probe.py --model gemini --reps 30
"""

import csv
import re
import random
import argparse
import time
from pathlib import Path
from datetime import datetime


# --- Prompt ---

SYSTEM_PROMPT = """You're participating in a linguistics study on sentence acceptability. You'll read a sentence and rate how natural it sounds on a 1-7 scale:

1 = Completely unacceptable
7 = Perfectly acceptable

Use the full range of the scale based on your intuitions as an English speaker. Give only the number."""


def build_user_prompt(sentence):
    """Build the user message for a single trial."""
    return f"""Please rate this sentence:

{sentence}

Rating (1-7):"""


# --- Model backends ---

def query_claude(system, user, model="claude-sonnet-4-6-20250514"):
    """Query Anthropic API with temperature."""
    from anthropic import Anthropic
    client = Anthropic()
    response = client.messages.create(
        model=model,
        max_tokens=5,
        temperature=0.7,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return response.content[0].text.strip()


def query_openai(system, user, model="gpt-4o"):
    """Query OpenAI API with temperature."""
    from openai import OpenAI
    client = OpenAI()
    response = client.chat.completions.create(
        model=model,
        max_tokens=5,
        temperature=0.7,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    return response.choices[0].message.content.strip()


def query_gemini(system, user, model="gemini-2.5-pro"):
    """Query Google Gemini API with temperature."""
    import google.generativeai as genai
    m = genai.GenerativeModel(model, system_instruction=system)
    config = genai.GenerationConfig(temperature=0.7, max_output_tokens=5)
    response = m.generate_content(user, generation_config=config)
    return response.text.strip()


BACKENDS = {
    "claude": query_claude,
    "gpt4o": query_openai,
    "gemini": query_gemini,
}


def parse_rating(text):
    """Extract a 1-7 integer from model response."""
    match = re.search(r'[1-7]', text)
    if match:
        return int(match.group())
    return None


# --- Main ---

def load_stimuli(path="stimuli.csv"):
    """Load stimuli from CSV."""
    items = []
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append(row)
    return items


def run_probe(model_name, n_reps=30, seed=42, output_dir="results"):
    """Run the full probe for one model."""
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)

    query_fn = BACKENDS[model_name]
    items = load_stimuli()
    rng = random.Random(seed)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    outfile = output_dir / f"ratings_{model_name}_{timestamp}.csv"

    total_trials = len(items) * n_reps
    trial_num = 0

    with open(outfile, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "rep", "model", "item_id", "noun", "det",
            "construction", "item_type", "sentence",
            "raw_response", "rating", "timestamp",
        ])
        writer.writeheader()

        for rep in range(1, n_reps + 1):
            # Randomize item order per rep
            rep_items = items.copy()
            rng.shuffle(rep_items)

            print(f"Rep {rep}/{n_reps}...")

            for item in rep_items:
                trial_num += 1
                user_prompt = build_user_prompt(item["sentence"])

                try:
                    raw = query_fn(SYSTEM_PROMPT, user_prompt)
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
                    "sentence": item["sentence"],
                    "raw_response": raw,
                    "rating": rating,
                    "timestamp": datetime.now().isoformat(),
                })

                if trial_num % 100 == 0:
                    print(f"  {trial_num}/{total_trials} trials complete")

                time.sleep(0.05)  # rate limiting

    print(f"Done. {total_trials} ratings written to {outfile}")
    return outfile


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run LLM judgment probe")
    parser.add_argument("--model", choices=["claude", "gpt4o", "gemini"],
                        default="claude", help="Which model backend")
    parser.add_argument("--reps", type=int, default=30,
                        help="Number of repetitions per item")
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for item ordering")
    args = parser.parse_args()

    run_probe(args.model, n_reps=args.reps, seed=args.seed)
