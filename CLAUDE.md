# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a theoretical linguistics paper arguing that English morphosyntactic countability is a homeostatic property cluster (HPC) maintained by bidirectional inference between form and meaning.

**Working title:** The Homeostatic Maintenance of English Countability: Bidirectional Inference and the Stability of Grammatical Clusters

**Author:** Brett Reynolds (Humber Polytechnic / University of Toronto)

**Target venues:** *Journal of Linguistics*, *Language*, *Linguistics* (Berlin)

## Document Structure

The paper is written in LaTeX with a standard article structure:

- `main.tex` — Primary document using `article` class with 12pt font, Charis SIL font (XeLaTeX), and APA citation style via biblatex
- `references.bib` — BibTeX bibliography (house style preamble loads this automatically)
- `NOTES.md` — Working notes including theoretical claims, terminology, predictions, and TODOs
- `.house-style/` — House style snapshot (version 1.0.0) with preamble, style rules, and style guide

## Building the Document

**IMPORTANT:** This document uses XeLaTeX (not pdfLaTeX) due to the house style preamble.

Build the LaTeX document using:
```bash
xelatex main.tex
biber main
xelatex main.tex
xelatex main.tex
```

Or with latexmk:
```bash
latexmk -xelatex main.tex
```

Clean auxiliary files:
```bash
latexmk -c
```

## Core Theoretical Architecture

### Three-Level Distinction (critical for all editing)

The paper maintains strict terminological hygiene between three levels of "countability":

1. **Discreteness** (ontological) — World structure
2. **Individuation** (semantic) — Linguistic construal
3. **Countability** (morphosyntactic) — Grammatical cluster

Do not conflate these terms. The paper's central claim is that morphosyntactic countability is an HPC maintained by bidirectional inference operating on individuation.

### The Dissociation Hierarchy

Count properties have an implicational structure ordered by "linkage tightness":

**Tight** (lost first): singular form, *a(n)*, low cardinals
**Moderate**: *several*, distributive quantifiers
**Loose** (retained longest): *many/few*, high round numerals, plural agreement

**Key prediction:** Properties dissociate tight → loose. No reverse pattern should exist.

### The Noun Classification

Example nouns are classified by their position in the dissociation hierarchy:

- **book** — Fully count (all properties)
- **people/person** — Fully count (suppletive singular)
- **folk** (BrE), **folks** (AmE) — Quasi-count (no singular, no *a(n)*, marginal low cardinals)
- **cattle**, **police** — Quasi-count (reject tight properties, accept loose)
- **furniture** — Mass (rejects all count properties)

### Functional Anchoring

Stable intermediates like *police* are explained by "functional anchoring" (the availability of *officer* as a singulative blocks drift toward full count status).

## House Style (Version 1.0.0)

This project uses Brett Reynolds house style conventions (snapshot at `.house-style/`). **All editing must follow house style rules.**

### Key House Style Conventions

**Mention vs. Quotation:**
- Use `\term{text}` for mention of forms and categories (produces italics)
- Use `\enquote{text}` for actual quotations (locale-aware quotes)
- Example: `\term{cattle}` is a quasi-count noun vs. As `\enquote{going forward}` spread...

**Dashes:**
- Parenthetical asides: en-dash with spaces (`the category is stable~-- within limits~-- across registers`)
- Ranges: en-dash without spaces (`2001--2025`, `pp.\ 113--127`)
- Compounds: hyphen only (`corpus-based study`)

**Linguistic Examples:**
- Uses `langsci-gb4e` package (NOT linguex, NO exe environment)
- Simple: `\ea\label{ex:label} \textit{Example text.} \z`
- Subexamples: `\ea \ea ... \ex ... \z \z`
- Judgements: `\ungram{*text}`, `\marg{?text}`, `\odd{\#text}`
- Glosses: `\gll ... \\ ... \\ \glt ...` with `\abbr{}` for small caps

**Writing Style:**
- Contractions preferred (don't, won't, can't)
- Paragraph target: ~60 words, max 100 words
- Avoid throat-clearers ("It is important to note that", "clearly", "obviously")
- Avoid hackneyed adverbs (moreover, furthermore, nevertheless)
- Prefer simple coordinators (and, but) and ordinal markers (first, second, finally)
- Use discourse markers for flow ("A first objection concerns...", "Consider first...")
- Never use `\paragraph{}` headings (use strong topic sentences instead)
- Avoid bold labels in prose (use narrative with transitions)

**Citations (biblatex with natbib=true):**
- Parenthetical: `\citep{key}` → (Author Year)
- Textual: `\textcite{key}` → Author (Year)
- With page: `\citep[113--127]{key}`

**Additional House Style Macros:**
- `\abbr{text}` — Small-caps abbreviations for glosses
- `\crossmark` — Cross-linguistic subscript marker (†)
- `\eg`, `\ie`, `\etc` — With proper spacing

**Full documentation:** See `.house-style/style-guide.md` and `.house-style/style-rules.yaml`

### LaTeX Conventions Specific to This Paper

- British English spelling (`babel` package with `british` option)
- APA citation style via biblatex
- Custom commands for this paper:
  - `\cmark` — Checkmark (✓)
  - `\xmark` — X mark (✗)
  - `\qmark` — Question mark (?) for marginal acceptability
- Tables use `booktabs` package

## Citation Management

All references are in `references.bib` organized by category:

- Core countability references (Allan, Grimm, Rothstein, Corbett, etc.)
- Syntactic approaches (Borer, Chierchia, Link)
- HPC and philosophy of kinds (Boyd, Millikan, Khalidi)
- Psycholinguistics and processing (Barner & Snedeker, Yoon)
- Typology and cross-linguistic (Haspelmath)
- Lexical resources (Husić et al.)

When adding citations, maintain this categorical structure and use consistent formatting.

### Recently Added Citations

- `khalidi2013` — Khalidi (2013), *Natural Categories and Human Kinds*
- `barner2005` — Barner & Snedeker (2005), quantity judgments and individuation

## Current Status

All sections are drafted. The paper has been through a review-board pass (March 2026) with revisions from advisory voices (Burke, Toulmin, Pullum, Royster, Adichie, Lunsford). Uncommitted revisions include title change ("English Countability"), ORCID link, keywords, abstract refinements, expanded introduction (Dahl 2016, Dennett 1991 pattern footnote, equilibrium framing), and section-divider reformatting throughout.

### Sections (all drafted)

- **Section 1 (Introduction)**: Puzzle of stable clustering, HPC framing, roadmap
- **Section 2 (Three levels)**: Ontological discreteness, semantic individuation, morphosyntactic countability; conventionalized vs. online construal
- **Section 3 (Mechanism)**: Bidirectional inference specified, weak homeostasis, mechanism weakening
- **Section 4 (Dissociation hierarchy)**: Implicational prediction, noun x property matrix, determiner requirement, demonstratives
- **Section 5 (Evidence)**: Heatmap figure, COCA corpus data, *folks* case
- **Section 6 (Alternative accounts)**: Feature-bundle, semantics-driven, syntacticist, prototype approaches, summary
- **Section 7 (Extensions)**: Cross-linguistic (singulatives, classifiers), diachronic (*pea*, *data*), functional anchoring
- **Section 8 (Outstanding issues)**: Plural-only nouns, processing predictions, acquisition predictions, formalising precision, scope and limitations
- **Section 9 (Conclusion)**: Synthesis, broader implications for grammatical categories

### Remaining Work

- Design and run acceptability probe (15-20 respondents; REB blocked)
- Check for diachronic evidence of ordered property loss (Allan 2011, Erbach)
- Revise based on probe results
- Final polish and submission

## Linguistic Notation

When writing linguistic examples:

- Use `\term{cattle}` for mentioned forms (not raw `\textit{}`)
- Uses `langsci-gb4e` package (NOT linguex, NO exe environment)
- Mark grammaticality: `\ungram{*text}`, `\marg{?text}`, `\odd{\#text}`
- Follow CGEL conventions (see user's global instructions for syntactic terminology)

## Falsifiability Criteria

The account is disconfirmed if:

1. A noun accepts *three N* but rejects *many N* (reverse implication)
2. A noun accepts *a(n) N* but requires *much N* not *many N* (the *a–many* split)
3. No intermediate cases show drift in either direction over time

## Probe Design (Section 5.2)

The planned acceptability study uses a 2×2×2 design:

- Determinative: tight (*three*) vs. moderate (*several*)
- Construction: existential vs. agentive
- Noun: *folks* vs. *people* (control)

Prediction: *three folks* shows larger existential–agentive difference than *three people* because existentials foreground individuation.

## Framework Compatibility Notes

- Compatible with CGEL descriptivism (systematizes "quasi-count" without generative apparatus)
- Compatible with predictive processing (high-precision predictions = tight linkage)
- Contrasts with Borer's DivP (explains lexical clustering, not just existence of count/mass syntax)
- Distinct from prototype theory (predicts ordered gradience, not just gradience)


## Multi-Agent Dispatch (MANDATORY)

Before dispatching multiple agents, ALWAYS ask Brett:
1. **Which model(s)?** Claude, Codex, Gemini, Copilot
2. **Redundant outputs?** Multiple models on same task for different perspectives?

See portfolio-level `CLAUDE.md` for CLI command patterns and full workflow.
