# Pre-registration: LLM Judgment Probe for Construction-Sensitivity of Countability

## Overview

This probe tests whether the dissociation hierarchy's construction-sensitivity prediction is recoverable from LLM outputs. It supplements COCA corpus data where critical cells are too sparse for direct estimation.

**Status:** Pre-registered. Commit SHA `dcd6ff4` recorded before any model was queried. This revision (v2) addresses methodological review; a new SHA will be recorded before data collection begins.

## Design

2 × 2 × 2 factorial, fully crossed:

| Factor | Levels |
|---|---|
| Noun | *people* (count), *folks* (boundary) |
| Determinative | *three* (tight), *several* (moderate) |
| Construction | existential, agentive |

No separate floor condition. Floor calibration comes from the filler set (see below).

## Stimuli

### Critical items (8 cells × 8 lexicalizations = 64 items)

Each cell has 8 lexically varied items. Verb phrases are matched across noun conditions AND across construction conditions to control for plausibility and aspect confounds.

#### VP set (shared across all conditions)

Each VP has an existential and agentive realization matched for aspect (all simple past or past progressive):

| # | Existential | Agentive |
|---|---|---|
| 1 | There were three/several [noun] waiting in the lobby. | Three/Several [noun] waited in the lobby. |
| 2 | There were three/several [noun] sitting on the bench. | Three/Several [noun] sat on the bench. |
| 3 | There were three/several [noun] standing by the door. | Three/Several [noun] stood by the door. |
| 4 | There were three/several [noun] walking down the hall. | Three/Several [noun] walked down the hall. |
| 5 | There were three/several [noun] gathered near the entrance. | Three/Several [noun] gathered near the entrance. |
| 6 | There were three/several [noun] lined up outside. | Three/Several [noun] lined up outside. |
| 7 | There were three/several [noun] crowding around the table. | Three/Several [noun] crowded around the table. |
| 8 | There were three/several [noun] chatting in the kitchen. | Three/Several [noun] chatted in the kitchen. |

### Fillers (48 items, four severity bands)

The filler set spans the full acceptability range. No filler involves countability boundary phenomena.

**Clearly acceptable (12):** Fully grammatical, semantically natural.
- The children played in the yard all afternoon.
- She locked the door before leaving the house.
- Two large dogs ran across the empty road.
- The manager approved the budget on Friday.
- Several old photographs were found in the attic.
- He finished reading the report before dinner.
- Three red cars were parked outside the building.
- The teacher explained the problem very clearly.
- Many tall trees line the edge of the park.
- She remembered to bring the keys this time.
- The train arrived exactly on schedule.
- Several new shops opened on the high street.

**Mildly degraded (12):** Grammatical but slightly odd (garden path, heavy NP, unusual word order, mild redundancy).
- The horse raced past the barn fell.
- The fact that the student who the professor liked failed surprised everyone.
- More people than just John showed up unexpectedly.
- What did you wonder whether she bought?
- The report that the committee submitted it was incomplete.
- Who do you think that saw the accident?
- The more carefully you plan the fewer problems arise.
- There seemed to appear to be a problem.
- What she said to him wasn't very clear to me at first.
- The old man the boats during the summer months.
- It was believed by everyone that she had already gone.
- Rarely does anyone ever remember to lock up properly.

**Clearly degraded (12):** Agreement violations, case errors, selection violations.
- The committee have made their decision and it are final.
- Him and me went to the store yesterday morning.
- She suggested him to leave the room immediately.
- The news were very surprising to all of us.
- He denied to have seen the suspect that evening.
- Them gave we the wrong directions to the hotel.
- She explained him the rules of the game carefully.
- The children was playing outside when it started raining.
- He insisted her to come along to the meeting.
- Us went to the park after the movie ended.
- She mentioned him that the deadline had been moved.
- The students has been working on the project all week.

**Ungrammatical (12):** Clear word-order violations.
- The walked dog the park in yesterday afternoon.
- She already been have left the building completely.
- Into put the bag the groceries she all of.
- The very ran quickly dog across the field today.
- Been sleeping is he since early this morning still.
- There cats two are the on mat sitting now.
- Gave the to her book he the wrong one.
- The from house the walked man slowly away then.
- Not she does understand the at question all here.
- Yesterday the were playing children outside in rain.
- To she tried the open but door was locked.
- Books the are on shelves the in wrong the order.

## Measurement

### Primary measure: surprisal

For each stimulus, compute the mean per-token surprisal (negative log-probability) of the full sentence under each model. Lower surprisal = more expected/acceptable. This avoids metalinguistic task demands and is the most reliable LLM-based proxy for acceptability (Hu & Levy 2023).

Implementation: use each model's log-probability API (or token-level log-probs from completion endpoints). Compute:

```
surprisal(sentence) = -1/N * sum(log P(token_i | token_1...token_{i-1}))
```

### Secondary measure: prompted Likert rating

As a convergent measure, also collect prompted 1-7 ratings using the elicitation below. These are reported alongside surprisal but are not the primary basis for the interaction test.

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

For Likert ratings: 10 repetitions per item per model at temperature = 0.7 (reduced from 30; surprisal is the primary measure and needs no repetition).

### Models

1. Claude Sonnet 4.6
2. GPT-4o (latest)
3. Gemini 2.5 Pro

### Trial counts

- Surprisal: 112 items × 3 models = 336 measurements (deterministic, no repetition needed)
- Likert: 112 items × 10 reps × 3 models = 3,360 ratings
- Total API calls: ~3,696

## Predictions

### Primary prediction (surprisal)

*Three folks* should show higher surprisal in the existential frame than the agentive frame. *Three people* should show no such asymmetry. *Several folks* should show no asymmetry. Formally:

```
[surprisal(three folks, exist) - surprisal(three folks, agent)]
  >
[surprisal(three people, exist) - surprisal(three people, agent)]
```

and:

```
[surprisal(several folks, exist) - surprisal(several folks, agent)]
  ≈
[surprisal(several people, exist) - surprisal(several people, agent)]
```

### Secondary prediction (Likert, convergent)

Same direction as surprisal but inverted scale (lower rating = more degraded):

- *Three folks* existential rated lower than agentive
- No such asymmetry for *three people* or *several folks*

### Filler calibration criterion

Mean surprisal must order: ungrammatical > clearly degraded > mildly degraded > acceptable. If this ordering fails for a model, that model's data are uninterpretable and are excluded from the interaction test (reported in supplementary materials).

### Disconfirmation

The prediction fails if:

- *Three folks* shows no existential-agentive surprisal difference (or the difference goes the wrong way)
- *Several folks* shows the same asymmetry as *three folks* (the effect isn't precision-specific)
- Fillers fail to calibrate for 2+ models (probe is uninformative)

## Analysis plan

### Step 1: Diagnostics (before any confirmatory analysis)

1. **Filler calibration.** Compute mean surprisal per filler band per model. If the four bands don't separate monotonically, exclude that model.
2. **Item-level surprisal distribution.** Plot surprisal for all 64 critical items. Flag any items where surprisal is invariant across conditions (the model isn't sensitive to the manipulation for that item).
3. **Likert response distribution.** If models produce degenerate Likert distributions (>90% at one value), report this and rely on surprisal only.

### Step 2: Confirmatory test (surprisal)

Linear mixed-effects model:

```r
surprisal ~ noun * det * construction + (1 | vp_lexicalization) + (1 | model)
```

Random intercepts for VP lexicalization (8 levels) and model (3 levels). The key test is the three-way interaction `noun:det:construction`.

### Step 3: Convergent test (Likert)

Ordinal regression on item-level mean ratings (aggregated across 10 reps to avoid pseudo-replication):

```r
mean_rating ~ noun * det * construction + (1 | vp_lexicalization) + (1 | model)
```

### Step 4: Reporting

- Report all cell means (surprisal and Likert) with 95% CIs
- Report the three-way interaction coefficient with CI from both models
- Plot the full distribution of surprisal values per cell
- Compare across the 3 LLM models; if they disagree, report each separately
- Report all diagnostics transparently, including failures

### Decision rules for failures

| Diagnostic | Threshold | Consequence |
|---|---|---|
| Filler bands don't separate | Non-monotonic mean surprisal | Exclude that model |
| Likert degenerate | >90% at one value | Report surprisal only for that model |
| Item invariant | Surprisal range < 0.1 across conditions | Flag item; run sensitivity analysis with and without |
| Models disagree on interaction direction | Opposite signs | Report each separately; do not aggregate; note as limitation |

## Known limitations

1. **Acceptability vs. grammaticality.** Surprisal measures expectedness, not grammaticality. Likert ratings measure acceptability. Neither directly measures grammatical well-formedness (Schutze 1996). This is appropriate here: the hierarchy predicts gradient degradation at the boundary, not a categorical distinction.

2. **No discourse context.** Stimuli are presented in isolation. Register context matters for *folks* especially. A future version could add discourse preambles.

3. **LLM ≠ speaker.** The probe targets model representations, not human grammatical competence. Convergence with the corpus record increases confidence; divergence is informative but not decisive.

4. **Pseudo-replication in Likert.** Temperature-based repetitions are draws from a single system, not independent participants. Likert analysis uses item-level aggregation to avoid inflating N. Surprisal, being deterministic, has no replication issue.

5. **Aspect matching is approximate.** Existential frames use progressive (*were waiting*); agentive frames use simple past (*waited*). This is inherent in the construction contrast. Both use past tense to minimize additional confounds.

## Registration

Before running any model:
1. Commit this file and `stimuli.csv` to git
2. Record the commit SHA: ____________ (v2)
3. v1 SHA: dcd6ff4 (initial pre-registration, before methodological review)
