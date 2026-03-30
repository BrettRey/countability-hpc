# Construction-Sensitivity Probe: COCA Queries

## Prediction

*Three folks* should be disproportionately rare in existential constructions (which foreground exact cardinality) compared to verb-following frames (which tolerate aggregate construal). *Three people* should show no such asymmetry. *Cattle* should reject both. *Many* should show no construction effect for any noun.

## Queries

Raw counts needed. 18 cells total.

### Existential: `there [be] [det] [noun]`

| Query | Cell |
|---|---|
| `there [be] three people` | E-3-people |
| `there [be] three folks` | E-3-folks |
| `there [be] three cattle` | E-3-cattle |
| `there [be] several people` | E-sev-people |
| `there [be] several folks` | E-sev-folks |
| `there [be] several cattle` | E-sev-cattle |
| `there [be] many people` | E-many-people |
| `there [be] many folks` | E-many-folks |
| `there [be] many cattle` | E-many-cattle |

### Verb-following: `[det] [noun] [v*]` (1R collocate)

| Query | Cell |
|---|---|
| `three people [v*]` | V-3-people |
| `three folks [v*]` | V-3-folks |
| `three cattle [v*]` | V-3-cattle |
| `several people [v*]` | V-sev-people |
| `several folks [v*]` | V-sev-folks |
| `several cattle [v*]` | V-sev-cattle |
| `many people [v*]` | V-many-people |
| `many folks [v*]` | V-many-folks |
| `many cattle [v*]` | V-many-cattle |

### Filtering

- For *cattle*: eyeball verb-following results for modifier uses (*three cattle ranchers*). Exclude those; report head-use count only.
- For *folks*: no filtering needed (doesn't function as modifier).
- For *people*: no filtering needed.

## Analysis

For each noun × determinative, compute:

**existential share** = E count / (E count + V count)

### The critical comparison

The prediction is confirmed if:

1. **existential share of *three folks* < existential share of *three people*** — the tight property is selectively suppressed in the high-precision frame
2. This asymmetry is **larger** than any asymmetry for *several* or *many* — the effect is specific to tight properties
3. *Many* shows similar existential shares for *people* and *folks* — loose properties are construction-insensitive

### What counts as disconfirmation

- *Three folks* shows the same existential share as *three people* → no construction-sensitivity → precision story loses support
- *Many folks* shows a lower existential share than *many people* → the effect isn't precision-specific → simpler frequency explanation suffices
- Counts too small to interpret (< 5 in critical cells) → inconclusive; note and move on

## Notes

- `there's three N` variant: track separately if easy. It may neutralize the precision demand (invariant existential = loose frame). Not essential.
- Consider also pulling *police* for comparison with *cattle*.
- Report exact counts. Don't compute percentages from cells under 10.
