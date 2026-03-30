# Pre-registration: LLM Judgment Probe for Construction-Sensitivity of Countability

## Overview

This probe tests whether the dissociation hierarchy's construction-sensitivity prediction is recoverable from LLM acceptability judgments. It supplements COCA corpus data where critical cells are too sparse for direct estimation.

**Status:** Pre-registered. The signed commit hash of this file must be recorded before any model is queried. File this at OSF or AsPredicted if submitting to a journal; at minimum, the git commit SHA serves as an immutable timestamp.

## Design

2 × 2 × 2 factorial, fully crossed:

| Factor | Levels |
|---|---|
| Noun | *people* (count), *folks* (boundary) |
| Determinative | *three* (tight), *several* (moderate) |
| Construction | existential, agentive |

Plus *cattle* as a quasi-count floor (tight rejection expected in both constructions).

## Stimuli

### Critical items (8 cells × 8 lexicalizations = 64 items)

Each cell has 8 lexically varied items. Verb phrases are matched across noun conditions (same VP appears with both *people* and *folks*) to control for plausibility differences.

#### VP set (shared across noun conditions)

1. waiting in the lobby
2. sitting on the bench
3. standing by the door
4. walking down the hall
5. gathered near the entrance
6. lined up outside
7. crowding around the table
8. chatting in the kitchen

#### Existential frame: There are [det] [noun] [VP].
#### Agentive frame: [Det] [noun] [VP-agentive variant].

Agentive VP variants (matched for plausibility):

1. signed the complaint
2. crossed the street
3. left the meeting early
4. arrived before noon
5. volunteered for the project
6. called the office
7. refused the offer
8. missed the deadline

### Cattle floor (8 items)

4 existential + 4 agentive, using *three* and *several*:
- There are three cattle in the field / near the barn.
- Three cattle escaped through the gate / wandered onto the road.
- There are several cattle in the field / near the barn.
- Several cattle escaped through the gate / wandered onto the road.

### Fillers (48 items, graduated severity)

The filler set spans the full acceptability range to prevent endpoint compression. Four bands:

**Clearly acceptable (12):** Fully grammatical, semantically natural.
- Many students attended the lecture.
- Several books were missing from the shelf.
- There are two birds in the tree.
- Three cars were parked outside.
- Many houses line the street.
- Several teachers joined the meeting.
- There are many options available.
- Two children played in the yard.
- Three windows were broken.
- Many visitors came to the museum.
- Several friends arrived together.
- There are three chairs in the room.

**Mildly degraded (12):** Grammatical but slightly odd (register mismatch, mild coercion, unusual collocation).
- There are many waters to choose from.
- Several evidences support the claim.
- Three beers were ordered at the bar.
- Many a folk has said the same.
- There are a great many persons involved.
- Several coffees sat cooling on the counter.
- Numerous youth gathered in the square.
- Various peoples have inhabited this region.
- There are a dozen odd cattle nearby.
- Many a people has risen and fallen.
- Several data points were missing.
- Numerous staff were let go.

**Clearly degraded (12):** Violations of count/mass syntax with quasi-count or mass nouns.
- There are three furnitures in the room.
- Several equipments were delivered.
- A cattle stood in the road.
- Many a police chased the suspect.
- There are three informations available.
- One police arrived at the scene.
- Several luggages were lost at the airport.
- A vermin ran across the floor.
- Three homeworks are due tomorrow.
- One clergy spoke at the service.
- Several knowledges were tested.
- A livestock grazed in the meadow.

**Ungrammatical (12):** Clear syntactic violations unrelated to countability.
- The walked dog the park in.
- She have been already left.
- Many is the people here.
- Him gave she the book.
- The children was playing outside.
- She don't knows the answer.
- There cats two are the on mat.
- He were going to the store yesterday.
- The very ran quickly dog.
- Them saw we at the party.
- Is been he sleeping since morning.
- The books is on the shelves.

## Agent specification

### Models

Run on 3 frontier models for robustness:
1. Claude Sonnet 4.6
2. GPT-4o (latest)
3. Gemini 2.5 Pro

### Elicitation method

No personas. The probe targets the model's representations, not simulated demographic variation. Each item is presented N = 30 times per model with temperature = 0.7 to capture response variability from the model itself.

Sprouse-style, 1-7 scale, no explanation requested:

```
System: You're participating in a linguistics study on sentence
acceptability. You'll read a sentence and rate how natural it
sounds on a 1-7 scale:

1 = Completely unacceptable
7 = Perfectly acceptable

Use the full range of the scale based on your intuitions as an
English speaker. Give only the number.

User: Please rate this sentence:

[Target sentence]

Rating (1-7):
```

### Trial structure

Each of the 120 items (64 critical + 8 cattle + 48 filler) is presented 30 times per model, in individually randomized orders. Total: 120 × 30 × 3 = 10,800 ratings.

## Predictions

### Primary prediction (construction × noun × determinative interaction)

| Cell | Prediction |
|---|---|
| three people, existential | high (6-7) |
| three people, agentive | high (6-7) |
| three folks, existential | **lower than agentive** (the key prediction) |
| three folks, agentive | moderate-high (4-6) |
| several people, existential | high (6-7) |
| several people, agentive | high (6-7) |
| several folks, existential | moderate-high (no asymmetry predicted) |
| several folks, agentive | moderate-high (no asymmetry predicted) |
| cattle (all) | low (1-3) |

### Operationalized

The prediction is confirmed if:

1. The existential-agentive difference for *three folks* is **larger** than for *three people* (interaction)
2. The existential-agentive difference for *several folks* is **not larger** than for *several people* (no interaction for moderate property)
3. *Cattle* items are rated low regardless of construction (floor)
4. Fillers discriminate across the four severity bands

### Disconfirmation

The prediction fails if:

- *Three folks* shows no existential-agentive difference (or the difference goes the wrong way)
- *Several folks* shows the same asymmetry as *three folks* (the effect isn't precision-specific)
- *Cattle* items are rated > 4 (floor not established)
- Fillers fail to span the range (all compressed to endpoints)

## Analysis plan

### Diagnostics (run first, before confirmatory analysis)

1. **Response distribution shape per item type.** If the model produces bimodal or degenerate distributions (all 7s or all 1s), flag this and report the distribution. Do not proceed to regression without verifying that the scale is used informatively.
2. **Filler calibration.** Compute mean and SD for each filler band. If the four bands don't separate (good > mildly degraded > clearly degraded > ungrammatical), the scale isn't functioning and results are uninterpretable.
3. **Within-model consistency.** Compute ICC across the 30 repetitions per item. If ICC < 0.3, the model is essentially random for that item.

### Confirmatory model

Ordinal regression (cumulative link model via R `ordinal` package):

```r
rating ~ noun * det * construction + (1 | item_lexicalization)
```

No random agent intercept (there are no agents; variance comes from temperature sampling). Random intercept for item lexicalization accounts for item-specific difficulty.

### Key contrast

The three-way interaction term `noun:det:construction` tests whether the existential-agentive asymmetry is larger for *folks* than *people* specifically with the tight determinative.

### Reporting

- Report all cell means with 95% CIs
- Report the three-way interaction coefficient with CI
- Plot the full distribution of ratings per cell (histograms or violin plots, not just means)
- Compare across the 3 models for robustness
- Report all diagnostics transparently, including any failures

### Sensitivity analysis

If models differ:
- Report each model separately
- Flag any model where filler calibration fails
- Do not aggregate across models unless all three pass diagnostics

## Interpretive constraints

Per the paper's framing:
- LLM outputs are detector-level responses, not direct evidence of grammatical status
- Results are interpreted against the COCA corpus record, not in place of it
- The probe tests whether the hierarchy's predicted extrapolation to sparse cells is recoverable, not whether LLMs have grammatical competence
- If models disagree, this is informative (sensitivity to architecture) rather than a failure

## Known limitations

1. **Acceptability vs. grammaticality.** The probe elicits acceptability ("how natural it sounds"), not grammaticality judgments. Acceptability reflects processing difficulty, frequency, pragmatic oddity, and prescriptive norms in addition to grammatical well-formedness (Schutze 1996). This is appropriate here: the hierarchy predicts gradient degradation at the boundary, not a categorical grammaticality distinction.

2. **No discourse context.** Stimuli are presented in isolation. Register context matters for *folks* especially (*three folks* in a folksy narrative may rate higher than in a formal frame). A future version could add discourse preambles, but the current design tests the baseline prediction without confounding context.

3. **Bounded scale compression.** The 1-7 Likert scale compresses extreme judgments. The graduated filler design (four severity bands) mitigates this by training the model to use the full range, but magnitude estimation would be an alternative worth exploring if the scale diagnostics show endpoint compression.

4. **LLM ≠ speaker.** The probe targets model representations, not human grammatical competence. Convergence with the corpus record increases confidence; divergence is informative but not decisive.

## Registration

Before running any model:
1. Commit this file and `stimuli.csv` to git
2. Record the commit SHA: 5115d3c
3. If submitting to a journal, file at OSF (osf.io) or AsPredicted (aspredicted.org) with the SHA as supplementary proof of timing
