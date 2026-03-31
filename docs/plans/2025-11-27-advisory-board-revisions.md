# Advisory Board Revisions Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement high-priority recommendations from the advisory board (Toulmin, Burke, Royster, Lunsford, Adichie, Pullum, Khalidi) to strengthen the paper's argumentation, narrative, and empirical grounding.

**Architecture:** The revisions focus on six high-priority areas: (1) foregrounding acquisition evidence as primary warrant, (2) distinguishing descriptive from mechanistic claims, (3) adding scope/positionality statements, (4) humanizing the narrative with anecdotes and representative nouns, (5) acknowledging social mechanisms of maintenance, (6) engaging more explicitly with formal semantics.

**Tech Stack:** XeLaTeX, biblatex-apa, house style (.house-style/preamble.tex), references.bib

---

## Task 1: Add Scoping Statement (Royster + Pullum)

**Files:**
- Modify: `main.tex:54-76` (Section 2, after three-level distinction)

**Step 1: Draft scoping statement**

Add after line 76 (end of §2):

```latex
\textbf{Scope.} The data here are drawn from descriptive grammars of contemporary standard English, primarily \textit{CGEL}; the hierarchy's applicability to other varieties, registers, and historical stages is an empirical question the framework generates but does not resolve. Register variation (e.g., agricultural speakers accepting \term{three cattle}) is not noise to be filtered but evidence for the precision-demand story: when communicative context raises the need for exact enumeration, even quasi-count nouns can be pressed into tight-linkage frames.
```

**Step 2: Verify LaTeX compiles**

Run: `xelatex main.tex`
Expected: No new errors, scoping statement appears in Section 2

**Step 3: Commit**

```bash
git add main.tex
git commit -m "docs: add scoping statement (Royster, Pullum)"
```

---

## Task 2: Distinguish Descriptive from Mechanistic Claims (Toulmin + Pullum)

**Files:**
- Modify: `main.tex:137` (end of §3.3, before transition to §4)

**Step 1: Add explicit distinction**

Replace line 137 with:

```latex
What we get, therefore, is an implicational hierarchy over the diagnostics: any noun that loses a loose property will already have lost all the tighter ones. The next section makes this hierarchy explicit and tests it against the quasi-count pattern.

\textbf{Descriptive vs.\ mechanistic claims.} The implicational hierarchy~-- tight properties lost before loose~-- is a descriptive generalisation that \textit{CGEL} documents but does not explain. Bidirectional inference is the proposed explanation. The hierarchy could stand even if the mechanistic account is revised or replaced; the mechanism's job is to derive the ordering, not merely to label it. Direct psycholinguistic evidence (acquisition overgeneralisation, priming effects) would strengthen the case that bidirectional inference operates in real time rather than being a post-hoc description of distributional patterns.
```

**Step 2: Verify LaTeX compiles**

Run: `xelatex main.tex`
Expected: No new errors, distinction appears at end of §3.3

**Step 3: Commit**

```bash
git add main.tex
git commit -m "docs: distinguish descriptive from mechanistic claims (Toulmin)"
```

---

## Task 3: Foreground Acquisition Evidence (Toulmin + Khalidi)

**Files:**
- Modify: `main.tex:109` (§3.2, acquisition paragraph)

**Step 1: Expand acquisition paragraph with Barner evidence**

Replace lines 109-110 with:

```latex
In acquisition, children don't learn count properties one by one. They learn that count morphosyntax correlates with individuation. When a noun exhibits some count properties, they generalize: this noun supports individuation, so other count frames should work~-- a pattern consistent with schema extension and entrenchment effects in usage-based morphology \citep{bybee2010}; cf.\ \textcite{tomasello2003}. The cluster is acquired as a unit because the construal, not each property, is what learners track.

Crucially, \textcite{barner2005} document exactly this overgeneralisation pattern in experimental and naturalistic data: children who hear \term{many} with a novel or quasi-count noun extend to low cardinals and \term{a}(\term{n}), treating one count property as evidence that others are licensed. This is inference, not mere correlation~-- the child infers from the presence of one property that the noun supports the construal that licenses the whole cluster. When the extension fails (e.g., \ungram{\term{three police}}), the error is evidence that the bidirectional link is productive, not a frozen lexical stipulation. Such overgeneralisations are the strongest evidence that the mechanism operates during acquisition and isn't simply a descriptive regularity.
```

**Step 2: Verify Barner citation exists in references.bib**

Run: `grep -i "barner2005" references.bib`
Expected: Entry found

**Step 3: Verify LaTeX compiles**

Run: `xelatex main.tex && biber main && xelatex main.tex`
Expected: No errors, Barner citation renders correctly

**Step 4: Commit**

```bash
git add main.tex
git commit -m "docs: foreground acquisition evidence as primary warrant (Toulmin, Khalidi)"
```

---

## Task 4: Add Social Mechanisms of Maintenance (Royster + Khalidi)

**Files:**
- Modify: `main.tex:122` (end of §3.2, after "inference-mediated coupling" sentence)

**Step 1: Add paragraph on social homeostasis**

Add after line 122:

```latex

\textbf{Levels of homeostasis.} The mechanisms described so far operate at the level of individual grammars: acquisition, processing, production. But grammatical categories are social kinds as well as cognitive ones. For standardised varieties, institutional norm-enforcement~-- style guides, editorial practice, language instruction, prescriptive grammars~-- constitutes an additional homeostatic mechanism, maintaining the cluster at the community level. The stability of standard English countability depends partly on these social institutions, which don't exist (or operate differently) for vernacular varieties or emergent dialects. \textcite{boyd1991}'s framework distinguishes individual-level mechanisms (genetic transmission, development) from population-level ones (reproduction, ecological niches); the linguistic analogue requires both cognitive mechanisms (the focus here) and social ones.
```

**Step 2: Verify LaTeX compiles**

Run: `xelatex main.tex && biber main && xelatex main.tex`
Expected: No errors, new paragraph appears in §3.2

**Step 3: Commit**

```bash
git add main.tex
git commit -m "docs: acknowledge social mechanisms of homeostasis (Royster, Khalidi)"
```

---

## Task 5: Narrativize Pease→Pea (Burke + Adichie)

**Files:**
- Modify: `main.tex:382-383` (§7.2, pease paragraph)

**Step 1: Rewrite pease case as narrative**

Replace lines 382-383 with:

```latex
Historical shifts provide evidence for the mechanism. Consider English \term{pea}. Speakers of Middle English heard \term{pease} with a final /z/ sound~-- the word for the vegetable, used in \term{pease porridge} and \term{pease pudding}. The noun was non-count: you had \term{much pease}, not \ungram{\term{many pease}}. But the final /z/ was phonologically identical to the plural suffix, and at some point speakers reinterpreted it as such. Once \term{pease} was heard as plural, the bidirectional inference mechanism kicked in: plural morphology cues individuation, so the noun should support other count properties. Speakers back-formed a singular \term{pea}, then extended the count cluster: \term{a pea}, \term{three peas}, \term{many peas}. The count cluster didn't just emerge; speakers \textit{built} it, one inference at a time.

If the historical record shows that looser properties (\term{many peas}, plural agreement) were established before tighter ones (\term{a pea}, \term{three peas}), that would confirm the predicted acquisition order. The diachronic evidence is suggestive but incomplete; what's clear is that the reanalysis triggered a cascade of count-property adoption, exactly as the homeostatic account predicts.
```

**Step 2: Verify LaTeX compiles**

Run: `xelatex main.tex`
Expected: No errors, narrative version appears in §7.2

**Step 3: Commit**

```bash
git add main.tex
git commit -m "docs: narrativize pease→pea case (Burke, Adichie)"
```

---

## Task 6: Add Hook Opening (Adichie)

**Files:**
- Modify: `main.tex:40-44` (§1, opening paragraph)

**Step 1: Rewrite opening with concrete puzzle**

Replace lines 43-44 with:

```latex
A student learning English writes \ungram{\term{I bought three furnitures}}. A copy editor debates whether \term{this data is} or \term{these data are} is correct. A Texan says \term{you folks} where a Bostonian says \term{you guys}. What do these have in common? They're all negotiations at the boundary of English countability~-- a boundary that turns out to be more structured than it first appears.

Count properties in English hang together strikingly: singular--plural contrast, \term{a}(\term{n}) selection, low cardinals, \term{many/few} vs.\ \term{much/little}, plural agreement, demonstratives, and distributive quantifiers almost always align. But quasi-count plurals such as \term{cattle} and \term{police} peel off the tightest properties first while keeping the looser ones. The pattern is implicational and stable over time, yet no existing account explains why.
```

**Step 2: Verify LaTeX compiles**

Run: `xelatex main.tex`
Expected: No errors, hook appears in §1 opening

**Step 3: Commit**

```bash
git add main.tex
git commit -m "docs: add hook opening with concrete puzzle (Adichie)"
```

---

## Task 7: Humanize Folks (Adichie)

**Files:**
- Modify: `main.tex:255` (§5.3, folks characterization)

**Step 1: Add humanizing paragraph**

Replace lines 255-256 with:

```latex
On the present account, this is exactly what we should expect for a noun whose individuation profile is weakening but hasn't fully collapsed. Morphologically, \term{folks} is simply a plural; it lacks a productive singular (\ungram{\term{a folks}}) just as the basic collective sense of \term{folk} lacks one (\ungram{\term{a folk}} in the ordinary 'people' sense).

The difference from \term{cattle} and \term{police} is semantic and pragmatic. When a Texan says \term{folks around here}, she's not just referring to people; she's claiming them as her own. Uses like \term{you folks}, \term{our folks back home}, and \term{the folks down the street} package the referents as in-group collectives with a strong solidarity flavour. The word's warmth~-- that sense of belonging and familiarity~-- is inseparable from its grammar. The individual atoms are still there ontically, but the noun's dominant sense foregrounds the group, backgrounding precise, enumerable units. The warmth comes at a grammatical cost: \term{folks} resists the precision that \term{three} demands.
```

**Step 2: Verify LaTeX compiles**

Run: `xelatex main.tex`
Expected: No errors, humanized version appears in §5.3

**Step 3: Commit**

```bash
git add main.tex
git commit -m "docs: humanize folks case (Adichie)"
```

---

## Task 8: Engage Formal Semantics (Pullum)

**Files:**
- Modify: `main.tex:444-448` (§8.4, formalising precision)

**Step 1: Expand formal semantics engagement**

Replace lines 444-448 with:

```latex
Another approach: define precision in terms of the granularity of the individuation required. Tight properties require fine-grained individuation (each atom distinctly bounded); loose properties tolerate coarse-grained individuation (atoms distinguished in aggregate but not individually tracked). This connects to work on granularity in mereology and event semantics.

Both approaches need to engage existing formal semantics more explicitly. \textcite{grimm2018} analyzes collectives and aggregates in terms of atomic accessibility: atoms exist in the denotation but aren't accessible to certain quantificational operations. \textcite{rothstein2010} distinguishes counting (cardinal) from measuring (approximating magnitude); \term{three cattle} fails as counting, but \term{many cattle} succeeds as measuring. \textcite{chierchia1998}'s nominal mass/count parameter turns on whether atoms are encoded in lexical semantics; quasi-count nouns would have atoms semantically present but with degraded accessibility.

The present account's notion of ``precision'' maps onto these frameworks as follows: tight properties require accessible, countable atoms (Grimm), exact cardinality (Rothstein), or encoding in lexical semantics (Chierchia). Loose properties tolerate inaccessible atoms, measure-based quantification, or pragmatic construal. The hierarchy is thus derivable from standard semantic frameworks if we rank count properties by their atomic-accessibility demands. A full formalisation would specify these demands as semantic presuppositions or selectional restrictions, deriving the ordering from independently motivated semantic primitives. I leave this for future work, noting only that the informal characterisation is sufficient for the empirical predictions developed here.
```

**Step 2: Verify all three citations (Grimm, Rothstein, Chierchia) exist**

Run: `grep -E "grimm2018|rothstein2010|chierchia1998" references.bib`
Expected: All three entries found

**Step 3: Verify LaTeX compiles**

Run: `xelatex main.tex && biber main && xelatex main.tex`
Expected: No errors, expanded formal discussion appears in §8.4

**Step 4: Commit**

```bash
git add main.tex
git commit -m "docs: engage formal semantics explicitly (Pullum)"
```

---

## Task 9: Let Cattle Travel Through Paper (Lunsford)

**Files:**
- Modify: `main.tex` (multiple sections)

**Step 1: Add forward reference to cattle in §2**

Insert after line 60 (end of ontological discreteness paragraph):

```latex
\term{Cattle}~-- the paradigm case examined throughout this paper~-- exemplifies the dissociation: ontologically discrete bovines, semantically construed as aggregates, morphosyntactically intermediate.
```

**Step 2: Add backward reference in §4**

Insert after line 174 (end of implicational prediction paragraph):

```latex
Recall \term{cattle} from \S2: ontologically discrete, semantically aggregated. The hierarchy predicts it should accept loose properties (plural agreement, \term{many}) while rejecting tight ones (singular, \term{a}(\term{n}), low cardinals). The matrix in \S5 confirms this.
```

**Step 3: Add backward reference in §6.2**

Insert after line 322 (end of purely semantic paragraph):

```latex
Returning to \term{cattle}: if its atoms are inaccessible (Grimm) or vaguely structured (Rothstein), why does \term{many cattle} work while \term{three cattle} fails? The present account's answer~-- they differ in precision demands~-- supplements rather than replaces these semantic analyses.
```

**Step 4: Verify LaTeX compiles**

Run: `xelatex main.tex`
Expected: No errors, cattle references appear throughout

**Step 5: Commit**

```bash
git add main.tex
git commit -m "docs: let cattle travel through paper as home-base noun (Lunsford)"
```

---

## Task 10: Add Broader Stakes to Conclusion (Adichie)

**Files:**
- Modify: `main.tex:472` (final paragraph of conclusion)

**Step 1: Rewrite final paragraph with stakes**

Replace line 472 with:

```latex
The broader implication is methodological. Grammatical categories need not be monolithic features or vague prototypes. They can be homeostatic property clusters~-- stable configurations maintained by causal mechanisms rather than definitional essences. Countability is one such cluster. Others~-- perhaps transitivity, finiteness, or the noun/verb distinction itself~-- may repay similar analysis.

If this is right, then the borders of grammar are not walls but gradients~-- maintained, negotiated, and occasionally redrawn by every speaker who uses them. The student who writes \ungram{\term{three furnitures}}, the editor who debates \term{data}, and the Texan who says \term{folks} aren't making errors so much as exploring the boundaries of a homeostatic system. Some explorations fail; others, over time, become the new equilibrium. \term{Pea} was once an error. So, perhaps, was \term{cattle} as a quasi-count noun. The cluster's stability is real, but it's a dynamic stability~-- held in place by millions of small inferences, every day, in every conversation.
```

**Step 2: Verify LaTeX compiles**

Run: `xelatex main.tex`
Expected: No errors, new conclusion appears

**Step 3: Commit**

```bash
git add main.tex
git commit -m "docs: add human stakes to conclusion (Adichie)"
```

---

## Task 11: Full Recompile and Verification

**Files:**
- Verify: `main.tex`, `main.pdf`

**Step 1: Clean auxiliary files**

```bash
rm -f main.aux main.bbl main.bcf main.blg main.log main.out main.run.xml
```

**Step 2: Full recompile**

```bash
xelatex main.tex && biber main && xelatex main.tex && xelatex main.tex
```

Expected: No errors, all citations resolved, PDF generated

**Step 3: Check page count**

Run: `pdfinfo main.pdf | grep Pages`
Expected: ~27-28 pages (increased from ~23 due to additions)

**Step 4: Verify no overfull hbox warnings exceed acceptable threshold**

Run: `grep "Overfull" main.log | wc -l`
Expected: Fewer than 10 (minor typesetting issues acceptable)

**Step 5: Final commit**

```bash
git add main.pdf
git commit -m "build: recompile after advisory board revisions"
```

---

## Task 12: Update README (Optional Documentation)

**Files:**
- Create: `docs/REVISIONS.md`

**Step 1: Document changes made**

```markdown
# Advisory Board Revisions - 2025-11-27

## Implemented Recommendations

### High Priority (Completed)

1. **Toulmin (Argumentation)**
   - ✓ Foregrounded acquisition evidence (Barner 2005) as primary warrant for bidirectional inference
   - ✓ Distinguished descriptive (hierarchy) from mechanistic (inference) claims
   - ✓ Qualified mechanism as inference to best explanation

2. **Burke (Rhetorical Ontology)**
   - ✓ Narrativized pease→pea case as representative anecdote
   - ✓ Named agents (learners, speakers, hearers) explicitly

3. **Royster (Positionality)**
   - ✓ Added scoping statement (CGEL, standard English)
   - ✓ Reframed register variation as evidence
   - ✓ Acknowledged social mechanisms of maintenance

4. **Lunsford (Pedagogy)**
   - ✓ Made cattle the home-base noun with forward/backward references

5. **Adichie (Narrative)**
   - ✓ Added hook opening with concrete puzzle
   - ✓ Humanized folks case (warmth, belonging)
   - ✓ Ended with broader stakes (grammar as gradient)

6. **Pullum (Descriptive Foundation)**
   - ✓ Engaged formal semantics (Grimm, Rothstein, Chierchia) in §8.4

7. **Khalidi (HPC Framework)**
   - ✓ Distinguished individual vs. community homeostasis

### Medium Priority (Deferred)

- Visual scaffold (triangular diagram) - requires TikZ, deferred
- For instructors footnote - out of scope for journal submission

## Files Modified

- `main.tex`: All nine sections revised
- Total additions: ~150 lines
- Page count: 23 → ~28 pages

## Next Steps

- Run folks probe (future empirical work)
- Stress-test hierarchy with larger noun sample (Pullum recommendation)
- Consider visual figure for revised submission
```

**Step 2: Save documentation**

```bash
git add docs/REVISIONS.md
git commit -m "docs: document advisory board revisions"
```

---

## Execution Notes

**Dependencies:**
- XeLaTeX installed and functional
- Biber for biblatex-apa
- references.bib must contain: barner2005, grimm2018, rothstein2010, chierchia1998, boyd1991
- House style files in .house-style/

**Testing Strategy:**
- Compile after each task to catch LaTeX errors early
- Verify citations exist before adding textcite/citep
- Check page count growth stays reasonable (<30 pages)

**Commit Strategy:**
- One commit per task (11 commits total)
- Descriptive messages reference advisory board members
- Final recompile commit includes PDF

**Time Estimate:**
- 2-3 minutes per task
- ~30 minutes total for full implementation
