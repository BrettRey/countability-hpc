# Decisions Log

Append-only record of project decisions. Agents: add an entry whenever a non-trivial decision is made during a session (structural changes, venue choices, theoretical commitments, scope changes, reviewer feedback acted on). Keep entries short.

Format: `## YYYY-MM-DD` then bullet points with **bold topic** and brief rationale.

---

## 2026-03-30

- **HPC book alignment.** Added field-relative projectibility (§2), stabilizer/mechanism distinction (§3.1), coupling spectrum, four-level stabilizer framework, two diagnostic tests (§3.2). Paper now reflects book's Ch 6-8 framework.
- **CxG credited explicitly.** New paragraph in §3.2 crediting Goldberg, Langacker, Bybee. HPC adds diagnostic toolkit (projectibility criteria, perturbation tests, field-relativity), not the mechanisms themselves. Framing from book Ch 1.
- **Precision formalized via field-relative projectibility.** §8.4 rewritten: the hierarchy is a morphosyntactic generalization; semantic accounts (Rothstein, Grimm, Chierchia) explain its shape but don't ground it. Dissolves Rothstein's counting/measuring objection.
- **Homeostasis vs shared-cause resolved.** Five perturbation arguments: data cascade, pease reverse cascade, police stability control, synonym divergence (fiction/lies), cross-linguistic divergence (hair/cheveux). All violate shared-cause indicator independence.
- **Precision-vs-frequency test.** PMI analysis with 8 determinatives shows precision, not frequency, drives the hierarchy. two (1.1M tokens, tight) repels cattle; numerous (35k, loose) attracts. Smoking gun for the hierarchy.
- **Projectibility foregrounded.** Abstract leads with "the clustering is projectible." Purpose named in §2: "predicting collocational and agreement behaviour from partial evidence." Conclusion adds projectibility payoff paragraph. Alternatives evaluated on stipulated vs explained projectibility.
- **LLM probe preregistered and run.** Zenodo DOI 10.5281/zenodo.19340604. Claude + GPT-5.4. Hierarchy confirmed (three folks 4.95/5.93 vs three people 7.00/6.92). Construction-sensitivity null (zero interaction). Moved to Appendix A.
- **\term{} = small caps, \mention{} = italics.** Global replacement of 749 \term{} to \mention{} for form mentions. \term{} reserved for concepts (countability, individuation, precision, quasi-count nouns, functional singulatives).
- **House palette for all figures.** houseprimary (blue), housesecondary (coral), houselight (grey). Symbols (✓/?/✗ → ? only) as redundant channel for accessibility. Legends horizontal above plots.
- **Dash cull.** 55 content dashes → 1 (closing sentence). Replaced with parentheses, commas, colons, semicolons per Bringhurst/house style.
- **Empirical base expanded.** 7 → 12 nouns + 3 singulatives. COCA existential probe, modifier rates, functional anchoring table, expansion table.
- **GitHub repo.** BrettRey/countability-hpc, CC BY 4.0.
- **§2 tightened.** Cut redundant itemized list and restatements. Saved ~1 page.
- **Redundant bar chart (old Fig 3) cut.** Dot plot with CIs supersedes it.

## 2026-03-30 (night session — reviewer feedback pass)

- **§3.2 broken into three subsections.** §3.2 "Why this produces homeostasis" (core argument + evidence), §3.3 "Stabilizers and functional anchoring" (weak homeostasis, CxG credit, coupling, multi-scale stabilizers, diagnostics), §3.4 "Homeostasis or shared cause?" (five perturbation arguments). Reviewer flagged overloading.
- **Number-morphology digression moved.** Removed from between tight and moderate hierarchy lists (broke the sequence). Placed after loose list, before determiner-requirement elaboration.
- **data/datum consolidated.** Primary treatment remains in §3.4 (shared-cause perturbation). §7.2 and §7.3 trimmed to one-sentence cross-references.
- **Syntacticist merged into feature-bundles.** Now §6.1 "Feature-bundle and syntacticist approaches." Both are formalist stipulation approaches; the Borer discussion preserved as a paragraph showing the problem recurs in functional heads. AE suggestion.
- **Conclusion rewritten to close on projectibility.** Cut two rhetorical paragraphs ("borders of grammar aren't walls"). Final paragraph now states the epistemic payoff.
- **"For a purpose" disaggregated.** §2 now distinguishes child (extending from partial evidence), parser (generating graded predictions), and grammarian (principled induction replacing arbitrary lists).
- **Terminology standardized.** "Tight-linkage properties" → "tight properties" throughout. "Quantifier" → "determinative" where it refers to the word class (CGEL convention). "Quantifier" retained for semantic operations.
- **Abstract trimmed.** 200 → 140 words. Cut property list, compressed examples, preserved HPC claim + hierarchy + projectibility.
- **§8.5 added: failure case (adverb).** Applies both diagnostics (projectibility test, homeostasis test) to traditional "adverb" and shows it fails both. Demonstrates the framework isn't vacuous.
- **Welsh cross-linguistic case expanded.** Added three-way paradigm (grawn/gronyn/gronynnau) from Grimm 2018 §2.1 with source-grounded examples. Added Maltese determinate plural for low cardinals.
- **Poisson CIs added to key corpus ratio.** three people 2,226/M (CI: 2,157–2,295) vs three folks 258/M (CI: 137–395); non-overlapping. Confirms 8.6× suppression is inferentially robust.
- **Long paragraphs split.** Acquisition evidence (257→two), HPC intro (195→two), corpus comparison (204→two), multi-scale stabilizers (183→two), alternatives summary (165→two), formalizing precision (164→two).

## 2026-03-31

- **v2 rewrite (main_v2.tex).** Complete rewrite with pattern-first structure: hierarchy (§3) and evidence (§4) before mechanism (§5). Per Schimel's review-board recommendation. Prose written fresh; figures/tables extracted to figures/ directory. 23 pages, ~9,000 words (from v1's 34/15,400).
- **Three-level discipline enforced in §2.** Ontology paragraph stays at world structure (farmer/librarian example). Individuation paragraph stays at construal (referents, not nouns). Morphosyntax paragraph introduces the cluster and labels. Syntax-101 analogy added.
- **Level-slippage audit.** "Expression demands" → "construal requires"; "individuation is bleached" → "speakers construe referents as roles"; "its individuation profile" → "the construal associated with"; figure caption fixed; number-morphology paragraph rewritten to flag bidirectional crossing as the mechanism.
- **"Kind" → "category".** Reserved "kind" for reporting Boyd's framework; "category" for the paper's own claims. "Natural class" → "predictable region on the hierarchy."
- **Conclusion leads with projectibility.** Per projectibility reviewer. Mechanism supports, doesn't lead.
- **Mechanism/stabilizer distinction clarified.** Bidirectional inference generates; anchoring, entrenchment, norms maintain.
- **Rothstein counting/measuring engaged.** Tight = counting, loose = measuring, but moderate tier (*several*) is where the hierarchy adds something the binary can't capture. Field-relative projectibility argument.
- **Circularity defence.** Implicational generalization (not definition), independent semantic motivation (Rothstein, Grimm), independent diagnostic (Barner & Snedeker quantity judgments).
- **LLM probe reframed.** Consistency check, not confirmation. N=2 models, not N=1,760. Zero-variance cells can't detect interactions.
- **G² robustness check added.** Log-likelihood confirms PMI pattern. p-values dropped; CIs only (Gelman).
- **Functional anchoring table expanded.** 7 pairs + folks control (from COCA data Brett provided).
- **Source grounding.** Bloom 1994a verified (Table 3.2 confirmed). Greenwood 1711 bib entry added. \enquote reserved for quotations; single quotes for glosses/senses.
- **Prototype section expanded.** PMI evidence explicitly connected to frequency-vs-precision divergence.
- **CxG positioning restored.** One paragraph in stabilizers section. "What CxG lacks isn't the ontology but the diagnostic toolkit."
- **Goodman cited.** "Projectible" glossed in abstract; Goodman 1955 + Boyd 1991 cited in §2.
- **Bold-label lists → prose.** Processing/acquisition predictions rewritten with ordinal markers. Appendix findings rewritten as prose.

