# Status

## Current state
**v4 (main_v4.tex/.pdf):** strongest current working draft. Keeps the v3 architecture (SPC → Khalidian causal structure → constrained Boydian homeostasis) and adds empirical scaffolding: diagnostic matrix, coding/head-use checks, expanded quasi-count sample, and auditable PMI/projectibility table. Built successfully on 2026-05-02; v4 is uncommitted.

**v3 (main_v3.tex/.pdf):** committed and pushed as `fda9c57` (`draft: add v3 countability paper`). Separate checkpoint that does not touch submitted/current drafts.

**v2 (main_v2.tex):** 23 pages, ~9,000 words. Pattern-first structure (hierarchy → evidence → mechanism). Preserved as the pre-rescue working draft.

**Linguistics submission package:** Blind manuscript, separate title page, and cover letter prepared in parallel files (`main_linguistics.tex/.pdf`, `linguistics_title_page.tex/.pdf`, `linguistics_cover_letter.md`). `main_v2` remains the main working draft.

**v1 (main.tex):** 34 pages, preserved as reference. All 17 original reviewer items addressed.

GitHub repo live (BrettRey/countability-hpc, CC BY 4.0).

## 2026-05-02 Session Notes (morning, Codex)

### Major work
- Created `main_v3.tex/.pdf` as a new version without touching existing drafts.
- Reframed the paper around SPC as the empirical floor, Khalidian causal structure as the realist interpretation, and Boydian homeostasis as an open maintenance hypothesis.
- Corrected the overclaim about homeostasis vs shared cause: `data/datum` and `pease/pea` are now compatible evidence, not decisive perturbation tests.
- Reframed functional anchoring as exact-count offloading rather than a demonstrated causal law.
- Added v3 tables: `figures/tab-coca-v3.tex`, `figures/tab-frequency-v3.tex`, `figures/tab-anchoring-v3.tex`.
- Built `main_v3.pdf`, committed v3 as `fda9c57`, and pushed to `origin/master` along with prior local commit `5ac11cb`.
- Created `main_v4.tex/.pdf` in place as the stronger empirical version, then revised it in response to review notes.
- Added v4 tables: `figures/tab-diagnostic-matrix-v4.tex`, `figures/tab-coding-v4.tex`, `figures/tab-expansion-v4.tex`, `figures/tab-projectibility-v4.tex`.
- Replaced the compact projectibility sign check with an auditable PMI/count table covering `two`, `three`, `each`, `every`, `several`, `various`, `many`, and `numerous`.
- Sharpened the precision tiers: `each/every` moved to tight; `several/various` treated as the least secure moderate tier.
- Softened projectibility and causal claims throughout v4: support in a focused domain, not proof of a broad predictive model; `organized by` rather than `maintained by` in the abstract.

### Verification
- `latexmk -xelatex -interaction=nonstopmode -halt-on-error main_v4.tex` builds `main_v4.pdf`.
- Final log scan found no overfull boxes, undefined refs, or citation errors. Only the existing informational `biblatex` `sortcites` notice remains.
- House-style scan found no long prose paragraphs, raw `\textit{}`, straight quote/backtick quote patterns, em dashes, or flagged throat-clearers in the revised v4 source.

### Current state
- Branch `master` is even with `origin/master`.
- v4 files are uncommitted and ready for review: `main_v4.tex`, `main_v4.pdf`, `figures/tab-diagnostic-matrix-v4.tex`, `figures/tab-coding-v4.tex`, `figures/tab-expansion-v4.tex`, `figures/tab-projectibility-v4.tex`.
- Other unrelated dirty/untracked files remain present and were not cleaned up: `DECISIONS.md`, `STATUS.md`, `.agent/`, `HPCstack.tex`, `README.md`, `countability-hpc.zip`, `linguistics_submission_info.md`, `literature`, `references.bib`.

### Next
- Review `main_v4.pdf` for argument flow and table readability.
- Decide whether to commit v4 as the new working draft.
- If moving toward submission, next empirical step is public token lists or a small regression model over noun, diagnostic, register, sense, and modifier/head status.

## 2026-03-31 Session Notes (afternoon, ~6 hours)

### Major work
- Complete v2 rewrite from scratch (pattern-first structure per Schimel)
- Three editorial review boards: writing (Sword/Basbøll/Schimel), content v1 (5 reviewers), content v2 (5 reviewers)
- §2 rewritten for level discipline (ontology/individuation/morphosyntax in their own lanes)
- Level-slippage audit across entire paper
- Rothstein counting/measuring engaged; moderate tier as wedge for field-relative projectibility
- Circularity defence written
- G² robustness check computed and added
- Functional anchoring table expanded (7 pairs + control) from Brett's COCA data
- Source grounding: Bloom 1994a verified, Greenwood 1711 bib entry, Barner & Snedeker verified
- House style pass: bold labels → prose, \enquote discipline, contractions, paragraph splits, p-values dropped

### Remaining work
- Brett doing manual read-through for voice, humour, rhetorical figures
- Handed to Codex for continuation of editorial pass

## 2026-03-31 Session Notes (late afternoon, Codex)

### Major work
- Chose `Linguistics` as the next submission target after comparing fit, metrics, cost, and overlap with Brett's current under-review queue
- Researched `Linguistics` submission requirements: ScholarOne portal, blind-review PDF submission, separate title page, abstract/keyword constraints, De Gruyter Mouton style expectations
- Created a separate blind submission manuscript (`main_linguistics.tex/.pdf`) rather than modifying `main_v2`
- Created `linguistics_title_page.tex/.pdf` with author details, acknowledgments, contribution statement, funding/COI note, and supporting-materials links
- Drafted `linguistics_cover_letter.md` and `linguistics_submission_info.md` for copy-paste into ScholarOne
- Built the blind manuscript and title page successfully; checked the blind PDF metadata/text for obvious author-identifying strings
- Committed the submission package as `5ac11cb` (`chore: add Linguistics submission package`)

### Current state
- Branch is `master`, ahead of `origin/master` by 1 commit (`5ac11cb`)
- `main_v2.tex` and `main_v2.pdf` were left untouched during submission prep
- `linguistics_submission_info.md` remains untracked as a helper file for the submission form

### Next
- Submit to `Linguistics` via ScholarOne using `main_linguistics.pdf` and `linguistics_title_page.pdf`
- Decide whether to keep `linguistics_submission_info.md` untracked or commit it later as a reusable submission helper

## 2026-03-30 Session Notes (morning → night, ~10 hours)

### Major work
- Aligned with HPC book (field-relative projectibility, coupling spectrum, stabilizer/mechanism, two diagnostics)
- Credited CxG; identified what HPC adds (diagnostic toolkit)
- Resolved homeostasis vs shared-cause with 5 perturbation arguments
- Resolved precision circularity via field-relative projectibility
- Ran COCA existential probe, modifier rates, precision-vs-frequency PMI
- Expanded to 12 nouns + 3 singulatives with functional anchoring table
- Preregistered LLM probe at Zenodo, ran on Claude + GPT-5.4
- Fixed all semantic macros (\term vs \mention), house palette, legends, dashes
- Three review board rounds (15 simulated reviewers total)

### Open items (17 from reviewer feedback)
1. ~~§3.2 overloaded — break into subsections~~ DONE (§3.2/3.3/3.4)
2. ~~Paragraph length — 8+ paragraphs over 150 words~~ DONE (worst offenders split)
3. Expand functional anchoring (N=3 → 8-10 noun pairs) — needs COCA queries
4. ~~Expand diachronic evidence (pease historical quotations)~~ DONE (1666 Boyle, 1711 Greenwood)
5. ~~Conclusion close on projectibility, not rhetoric~~ DONE
6. ~~Disaggregate "for a purpose" by user class (child/parser/grammarian)~~ DONE
7. ~~Consolidate data/datum (appears in 3 places)~~ DONE (primary in §3.4, others cross-ref)
8. ~~Move number-morphology digression out of hierarchy lists~~ DONE (after loose list)
9. ~~Standardize terminology (tight-linkage/tight; determinative/quantifier)~~ DONE
10. ~~Trim abstract to ~150 words~~ DONE (140 words)
11. ~~Fix cross-reference S5.2/S5.4~~ DONE (all \ref{} auto-update, no hardcoded numbers)
12. ~~Stress-test field-relative projectibility against a failure case~~ DONE (§8.5 adverb)
13. ~~Tighten acquisition claims (Shirai)~~ DONE (prototype-to-periphery parallel cited)
14. ~~Cross-linguistic case from Grimm 2018~~ DONE (Welsh three-way paradigm, Maltese)
15. ~~Inferential statistics on key ratios (Gries)~~ DONE (Poisson CIs, non-overlapping)
16. ~~Merge syntacticist section into feature-bundles (AE suggestion)~~ DONE
17. ~~Survey diachronic evidence for predicted ordering (AE suggestion)~~ DONE (noted limitation; prediction stated explicitly; broader survey flagged as future work)

### All 17 items complete.
