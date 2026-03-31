# Reviewer Feedback Revisions Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Address all 17 open items from three rounds of review-board feedback, bringing the paper to submission-ready state.

**Architecture:** Four phases ordered by dependency: structural reorganization first (moves text, changes line numbers), then content expansion (needs source-grounding), then argument refinement, then polish. Within each phase, independent tasks can run in parallel.

**Tech Stack:** LaTeX (XeLaTeX build), COCA corpus data, house-style macros (`\term{}`, `\mention{}`, `\enquote{}`), biblatex with natbib.

---

## Phase 1: Structural Reorganization

Do these first. They move text between sections, so all subsequent edits should reference the post-Phase-1 structure. Build and verify after each task.

### Task 1: Break §3.2 into subsections (Item #1)

**Problem:** §3.2 "Why this produces homeostasis" (lines 111–148) is ~38 paragraphs covering 7 distinct topics: homeostatic pressure, acquisition evidence, processing/production, weak homeostasis, CxG credit, multi-scale stabilizers, diagnostics, and homeostasis-vs-shared-cause. Reviewers flagged it as overloaded.

**Files:**
- Modify: `main.tex:111–148`

**Proposed structure:**

```
\subsection{Why this produces homeostasis}\label{sec:homeostasis}
  [lines 111–113: core homeostatic argument]
  [lines 114–123: acquisition, processing, production evidence]

\subsection{Stabilizers and functional anchoring}\label{sec:stabilizers}
  [lines 124–128: weak homeostasis, police/officer]
  [lines 130: CxG credit paragraph]
  [lines 132: coupling description]
  [lines 134: multi-scale stabilizers]
  [lines 136: two diagnostics]

\subsection{Homeostasis or shared cause?}\label{sec:shared-cause}
  [lines 138–148: the five perturbation arguments]
```

- [ ] **Step 1:** Read lines 111–148 carefully; identify natural break points between the three proposed subsections.
- [ ] **Step 2:** Insert `\subsection{Stabilizers and functional anchoring}\label{sec:stabilizers}` before the weak-homeostasis paragraph (currently starts "The homeostatic pressure is real but not deterministic" at line 124).
- [ ] **Step 3:** Insert `\subsection{Homeostasis or shared cause?}\label{sec:shared-cause}` before "A residual question" (line 138).
- [ ] **Step 4:** Check all `\ref{sec:homeostasis}` cross-references still point sensibly. Update any that should point to the new subsection labels.
- [ ] **Step 5:** Build (`xelatex main.tex && biber main && xelatex main.tex && xelatex main.tex`) and verify no broken references.
- [ ] **Step 6:** Commit: "refactor: break §3.2 into three subsections"

### Task 2: Move number-morphology digression out of hierarchy lists (Item #8)

**Problem:** Line 250 is a 195-word paragraph about productive number morphology (`-s` constituting individuation, zero-plural nouns, modifier position) embedded between the "Tight linkage" and "Moderate linkage" itemized lists in §4. It breaks the flow of the hierarchy presentation.

**Files:**
- Modify: `main.tex:242–268`

- [ ] **Step 1:** Read lines 242–268 to confirm the digression boundaries.
- [ ] **Step 2:** Cut the number-morphology paragraph (line 250) from between the tight and moderate lists.
- [ ] **Step 3:** Paste it after the hierarchy lists end and before the determiner-requirement paragraph (line 265), or convert it to a footnote on the "Singular–plural contrast" list item if it's compact enough. Alternatively, move it to §8 (Outstanding issues) if it fits better there.
- [ ] **Step 4:** Ensure the tight → moderate → loose list reads as a clean uninterrupted sequence.
- [ ] **Step 5:** Build and verify.
- [ ] **Step 6:** Commit: "refactor: move number-morphology digression out of hierarchy lists"

### Task 3: Consolidate data/datum discussion (Item #7)

**Problem:** The data/datum case appears in at least 4 locations: §1 intro (line 58), §3.2 shared-cause arguments (lines 140–141), §7.2 diachronic predictions (line 923), §7.3 functional anchoring (line 959), and conclusion (lines 1037, 1043). Reviewers want consolidation.

**Files:**
- Modify: `main.tex` at lines 58, 140–141, 923, 959, 1037, 1043

**Strategy:** Keep the primary treatment in the shared-cause section (§3.2/new §3.4, lines 140–141) where it does the most argumentative work (forward cascade perturbation). Reduce other mentions to brief back-references using `\S\ref{}`.

- [ ] **Step 1:** Read all six data/datum passages and map their argumentative function.
- [ ] **Step 2:** Identify the primary home (shared-cause section) and which other passages are redundant vs. necessary for local argument.
- [ ] **Step 3:** In §7.2 (line 923) and §7.3 (line 959): trim to one-sentence cross-references ("The \mention{data}/\mention{datum} case (\S\ref{sec:shared-cause}) illustrates the same logic").
- [ ] **Step 4:** In the conclusion (lines 1037, 1043): keep brief mentions (these are summary contexts, one sentence each is fine).
- [ ] **Step 5:** In the intro (line 58): keep the brief mention (it's a hook).
- [ ] **Step 6:** Build and verify.
- [ ] **Step 7:** Commit: "refactor: consolidate data/datum discussion"

### Task 4: Merge syntacticist section into feature-bundles (Item #16)

**Problem:** The "Syntacticist approaches" subsection (§6.3, lines 876–882) covers Borer's DivP approach. A reviewer suggested merging it into "Feature-bundle approaches" (§6.1, lines 858–864) since both are formalist accounts that stipulate rather than explain the hierarchy.

**Files:**
- Modify: `main.tex:858–882`

- [ ] **Step 1:** Read both subsections (858–864 and 876–882).
- [ ] **Step 2:** Evaluate whether the merge is warranted. The syntacticist section makes a distinct point (countability in functional heads vs. lexical features). If the points are genuinely different, keep them separate but add a bridging sentence. If they overlap substantially, merge.
- [ ] **Step 3:** If merging: rename §6.1 to "Feature-bundle and syntacticist approaches", integrate the Borer material, and remove the §6.3 subsection heading.
- [ ] **Step 4:** Update the §6 summary (line 898–900) if section structure changed.
- [ ] **Step 5:** Build and verify.
- [ ] **Step 6:** Commit: "refactor: merge syntacticist into feature-bundle section"

---

## Phase 2: Content Expansion

These tasks add new material. Several require source-grounding (reading literature before writing). Independent tasks can run in parallel.

### Task 5: Expand functional anchoring table (Item #3)

**Problem:** Table 5 (lines 939–955) has only 3 quasi-count/singulative pairs (police/officers, poultry/chickens, clergy/priests). Reviewers want 8–10 pairs.

**Files:**
- Modify: `main.tex:939–955` (Table 5)
- Sources needed: COCA for frequency data

**Candidate pairs to add:**
- cattle/cows (already discussed in text but not in the table)
- livestock/animals (or livestock/sheep, livestock/goats)
- vermin/rats (or vermin/pests)
- youth/youngsters (or youth/teenagers)
- folk(s)/people (the control case — person serves the function)
- gentry/gentlemen (historical)

- [ ] **Step 1:** Identify 5–7 additional quasi-count/singulative pairs from the nouns already in the paper (cattle, livestock, vermin, youth, folks) plus candidates from CGEL or the literature.
- [ ] **Step 2:** For each pair, look up COCA frequencies for `three [noun]` (head uses only, filtering modifier uses where needed). **Source-grounding required:** do not estimate frequencies; run the actual COCA queries or note that Brett needs to run them.
- [ ] **Step 3:** Add rows to Table 5. Compute per-million rates and ratios.
- [ ] **Step 4:** Update the text around the table (lines 937, 957) to reference the expanded set.
- [ ] **Step 5:** Build and verify table formatting.
- [ ] **Step 6:** Commit: "content: expand functional anchoring table to 8–10 pairs"

### Task 6: Expand diachronic evidence — pease historical quotations (Item #4)

**Problem:** The pease → pea case (lines 917–921) is described narratively but lacks dated historical quotations showing the cascade. Reviewers want evidence that loose properties appeared before tight ones.

**Files:**
- Modify: `main.tex:917–925`
- Sources needed: OED entry for *pea* (cited as `oed` in references); historical corpora (EEBO, COHA) if available

- [ ] **Step 1:** **Source-grounding required.** Read the OED entry for *pea, n.¹* to find earliest attestations of: (a) plural *peas/pease* with count syntax, (b) singular *pea* back-formation, (c) *a pea*, (d) low cardinals with *pea(s)*. Check whether loose properties (many peas, plural agreement) are attested before tight ones (a pea, three peas).
- [ ] **Step 2:** If OED data confirms the ordering, add 2–3 dated quotations to the diachronic section showing the cascade.
- [ ] **Step 3:** If OED data is ambiguous or unavailable, note this honestly: "The diachronic ordering is suggestive but the historical record doesn't clearly resolve the sequence."
- [ ] **Step 4:** Build and verify.
- [ ] **Step 5:** Commit: "content: add historical quotations for pease → pea cascade"

### Task 7: Survey diachronic evidence for predicted ordering (Item #17)

**Problem:** Related to Task 6 but broader. A reviewer suggested surveying whether other historical mass→count or count→mass shifts show the predicted tight-before-loose ordering.

**Files:**
- Modify: `main.tex:917–925` (diachronic predictions section)
- Sources needed: Allan 2011, Erbach (if available in literature/), historical corpus studies

- [ ] **Step 1:** **Source-grounding required.** Check `literature/` for Allan 2011 and Erbach papers on diachronic countability shifts. Read them.
- [ ] **Step 2:** Identify 2–3 additional nouns with documented count↔mass shifts (besides pea and data). Good candidates: *news* (count → mass), *pease*, *corn* (BrE mass/AmE count divergence).
- [ ] **Step 3:** For each, note whether the evidence supports tight-before-loose ordering in either direction.
- [ ] **Step 4:** Add a paragraph to §7.2 summarizing the diachronic evidence.
- [ ] **Step 5:** Build and verify.
- [ ] **Step 6:** Commit: "content: survey diachronic ordering evidence"

### Task 8: Cross-linguistic case from Grimm 2018 (Item #14)

**Problem:** §7.1 (lines 906–915) mentions Welsh singulatives from Grimm 2018 but keeps it brief. Reviewers want a worked example.

**Files:**
- Modify: `main.tex:906–915`
- Sources needed: Grimm 2018 (check `literature/` for PDF/MD)

- [ ] **Step 1:** **Source-grounding required.** Read Grimm 2018 for the Welsh singulative data. Find the specific paradigm showing collectives accepting loose quantifiers but resisting low numerals/distributives.
- [ ] **Step 2:** Add a concrete example (with glosses using `\gll` if appropriate, or inline if simple) showing the tight/loose split in Welsh collectives.
- [ ] **Step 3:** Keep addition to ~100 words. The section is explicitly "programmatic"; one worked example suffices.
- [ ] **Step 4:** Build and verify.
- [ ] **Step 5:** Commit: "content: add Welsh singulative worked example from Grimm 2018"

### Task 9: Stress-test field-relative projectibility (Item #12)

**Problem:** Reviewers want to see the framework tested against a failure case — a category that *looks* like an HPC but fails the projectibility or homeostasis tests.

**Files:**
- Modify: `main.tex:1001–1013` (§8.4 Formalizing precision) or `main.tex:1015–1021` (§8.5 Scope and limitations)

- [ ] **Step 1:** Identify a candidate failure case. Best option: the traditional category "adverb" — already mentioned at line 136 as "perturbation-inert." Alternatively: transitivity, or a cross-linguistic category that doesn't cluster.
- [ ] **Step 2:** Write a paragraph (~80 words) applying the two diagnostics (projectibility test, homeostasis test) to the failure case and showing it fails. This demonstrates the framework isn't vacuous.
- [ ] **Step 3:** Place it in §8.4 or §8.5, whichever flows better.
- [ ] **Step 4:** Build and verify.
- [ ] **Step 5:** Commit: "content: stress-test projectibility against failure case"

### Task 10: Tighten acquisition claims with Shirai (Item #13)

**Problem:** §8.3 (lines 989–999) makes acquisition predictions but a reviewer flagged that Shirai's work on aspect hypothesis should be cited or engaged with, since it's relevant to ordered acquisition.

**Files:**
- Modify: `main.tex:989–999`
- Sources needed: Shirai (check which Shirai paper — likely Shirai & Andersen 1995 on Aspect Hypothesis, or Shirai 2004)

- [ ] **Step 1:** **Source-grounding required.** Check whether Shirai is in `references.bib` or `references-local.bib`. If not, identify the correct Shirai reference. Read the source.
- [ ] **Step 2:** Determine whether Shirai's ordered-acquisition findings for aspect parallel the predicted ordered acquisition for countability. If yes, cite as an analogous case. If the analogy is weak, note the difference.
- [ ] **Step 3:** Tighten the acquisition predictions paragraph to be more specific about what evidence would count for/against, citing Shirai where appropriate.
- [ ] **Step 4:** Add bib entry to `references-local.bib` if needed.
- [ ] **Step 5:** Build and verify.
- [ ] **Step 6:** Commit: "content: tighten acquisition claims, cite Shirai"

### Task 11: Inferential statistics on key ratios (Item #15)

**Problem:** The corpus evidence (§5.2) reports raw ratios (e.g., 8.6-fold suppression of *three folks*) but a reviewer (citing Gries) wants inferential statistics — at minimum confidence intervals or a significance test on the key comparisons.

**Files:**
- Modify: `main.tex:433–466` (corpus evidence section)
- Possibly create: a small R or Python script to compute CIs

**Strategy:** The simplest approach is exact Poisson CIs on the per-million rates (already partly done for the dot plot, Figure 3). Adding a brief note that the key ratios have non-overlapping CIs would satisfy the reviewer without requiring a full statistical apparatus.

- [ ] **Step 1:** Identify the 2–3 key comparisons that need inferential support: (a) *three people* vs. *three folks* per-million rate, (b) *many people* vs. *many folks* per-million rate, (c) the ratio of suppression (tight vs. loose).
- [ ] **Step 2:** Compute 95% Poisson CIs for these rates. The counts and denominators are in Table 1 (line 437–454). Formula: for count $k$ and denominator $n$, rate = $k/n \times 10^6$, CI via `qpois(c(0.025, 0.975), k) / n * 1e6`.
- [ ] **Step 3:** Add a sentence or two to §5.2 reporting non-overlapping CIs for the key comparison. Reference Gries if Brett confirms the specific Gries citation.
- [ ] **Step 4:** Build and verify.
- [ ] **Step 5:** Commit: "content: add inferential statistics to key corpus ratios"

---

## Phase 3: Argument and Framing Refinement

These tasks don't add new data but sharpen the argument.

### Task 12: Conclusion close on projectibility (Item #5)

**Problem:** The conclusion's final paragraph (lines 1041–1043) ends on rhetoric ("The cluster's stability is real, but it's a dynamic stability..."). Reviewers want it to close on the epistemic payoff — what projectibility buys you.

**Files:**
- Modify: `main.tex:1041–1043`

- [ ] **Step 1:** Read the current conclusion ending (lines 1033–1043).
- [ ] **Step 2:** Rewrite the final paragraph to close on projectibility rather than "every conversation." The key point: the HPC analysis isn't just a description; it tells you which predictions are licensed, which aren't, and why. That's what makes it worth having.
- [ ] **Step 3:** Keep the rewrite under 100 words. Cut the "borders of grammar aren't walls" rhetoric if space is needed.
- [ ] **Step 4:** Build and verify.
- [ ] **Step 5:** Commit: "framing: close conclusion on projectibility payoff"

### Task 13: Disaggregate "for a purpose" by user class (Item #6)

**Problem:** Line 82 says projectibility is "for the purpose of predicting collocational and agreement behaviour from partial evidence: a learner, parser, or grammarian." A reviewer wants these unpacked — the purpose differs for each user.

**Files:**
- Modify: `main.tex:82`

- [ ] **Step 1:** Read the paragraph at line 82.
- [ ] **Step 2:** Expand the single sentence into 2–3 sentences distinguishing user classes. Something like: "For the learner, it means that encountering *many* licenses extending to plural agreement. For the parser, it means that processing one count property generates predictions for others. For the grammarian, it means that the category supports reliable generalizations rather than arbitrary lists."
- [ ] **Step 3:** Keep addition under 60 words (this is within a paragraph that's already 154 words).
- [ ] **Step 4:** Build and verify.
- [ ] **Step 5:** Commit: "framing: disaggregate projectibility by user class"

---

## Phase 4: Polish and Cleanup

Do these last, after all structural and content changes are complete.

### Task 14: Break long paragraphs (Item #2)

**Problem:** 11 paragraphs exceed 150 words (lines 60, 82, 117, 134, 136, 250, 460, 462, 464, 900, 1013). House style targets ~60 words, max 100.

**Files:**
- Modify: `main.tex` at lines 60, 82, 117, 134, 136, 250, 460, 462, 464, 900, 1013

**Note:** Some of these may already be addressed by earlier tasks (line 250 by Task 2; line 82 by Task 13; line 134 may be split by Task 1). Re-check after Phases 1–3.

- [ ] **Step 1:** After Phases 1–3 are complete, re-run the word-count check to find remaining long paragraphs.
- [ ] **Step 2:** For each over-length paragraph, find a natural break point (topic shift, example transition, or claim-then-evidence boundary).
- [ ] **Step 3:** Split into two shorter paragraphs. Ensure each has a clear topic sentence.
- [ ] **Step 4:** Build and verify.
- [ ] **Step 5:** Commit: "style: break long paragraphs to house style targets"

### Task 15: Standardize terminology (Item #9)

**Problem:** The paper uses both "tight-linkage" and "tight" (and "loose-linkage"/"loose") interchangeably. Similarly, "determinative" (CGEL category term) and "quantifier" (function/semantic term) aren't always distinguished consistently.

**Files:**
- Modify: `main.tex` (16 instances of linkage terms, 39 of determinative/quantifier)

- [ ] **Step 1:** Grep for all variants: `tight-linkage`, `tight linkage`, `loose-linkage`, `loose linkage`, bare `tight`/`loose` used as technical terms.
- [ ] **Step 2:** Standardize to: first use introduces both forms ("tight-linkage properties (henceforth: tight properties)"), then use the short form throughout.
- [ ] **Step 3:** Grep for `quantifier` vs. `determinative`. In CGEL terms, *many*, *several*, *three* are determinatives functioning as determiners. "Quantifier" is a semantic/functional label. Ensure the paper uses "determinative" for the word class and "quantifier" only when discussing the semantic operation.
- [ ] **Step 4:** Build and verify.
- [ ] **Step 5:** Commit: "style: standardize tight/loose and determinative/quantifier terminology"

### Task 16: Trim abstract to ~150 words (Item #10)

**Problem:** The abstract (lines 42–48) is currently ~210 words. Target: ~150.

**Files:**
- Modify: `main.tex:42–48`

- [ ] **Step 1:** Count exact word count of current abstract.
- [ ] **Step 2:** Identify cuts. Candidates: the parenthetical examples in the first sentence, the list of count properties (replace with "count properties"), the detail about construction-sensitivity. The hierarchy and HPC claim must stay.
- [ ] **Step 3:** Rewrite to ~150 words. Preserve: (1) the puzzle (tight clustering + ordered dissociation), (2) the HPC claim, (3) bidirectional inference as mechanism, (4) the precision hierarchy, (5) projectibility payoff.
- [ ] **Step 4:** Build and verify.
- [ ] **Step 5:** Commit: "style: trim abstract to ~150 words"

### Task 17: Fix cross-reference S5.2/S5.4 (Item #11)

**Problem:** A reviewer noted a cross-reference error between S5.2 (Corpus evidence) and S5.4 (CGEL's quasi-count nouns). Since the paper uses `\S\ref{}`, this may be a narrative reference ("as shown in the corpus section") pointing to the wrong subsection, or a label that shifted when sections were reorganized.

**Files:**
- Modify: `main.tex` (location TBD)

- [ ] **Step 1:** After all structural changes (Phase 1), build the paper and search the PDF for "S5" or "§5" references.
- [ ] **Step 2:** Grep for all `\ref{sec:` cross-references and verify each points to the correct section.
- [ ] **Step 3:** Fix any mismatches.
- [ ] **Step 4:** Build and verify.
- [ ] **Step 5:** Commit: "fix: correct cross-references"

---

## Execution Notes

### Dependencies
- **Phase 1 must complete before Phase 4** (paragraph splitting and terminology standardization depend on final text positions).
- **Tasks within a phase are independent** and can run in parallel.
- **Phase 2 tasks that require source-grounding** (Tasks 6, 7, 8, 10) need literature files read before writing. Brett may need to provide OED access or COCA query results.

### Source-Grounding Checklist
Before executing Phase 2, verify these sources are available in `literature/`:
- [ ] Grimm 2018 (for Task 8: Welsh singulatives)
- [ ] Allan 2011 (for Task 7: diachronic survey)
- [ ] Erbach (for Task 7: diachronic survey)
- [ ] Shirai (for Task 10: acquisition)
- [ ] Gries (for Task 11: statistical methods citation)
- [ ] OED entry for *pea* (for Task 6: historical quotations)

### Build Command
```bash
xelatex main.tex && biber main && xelatex main.tex && xelatex main.tex
```

### Estimated Scope
- Phase 1 (structural): 4 tasks, moderate complexity
- Phase 2 (content): 7 tasks, high complexity (source-dependent)
- Phase 3 (framing): 2 tasks, low complexity
- Phase 4 (polish): 4 tasks, low-moderate complexity
- **Total: 17 tasks across 4 phases**
