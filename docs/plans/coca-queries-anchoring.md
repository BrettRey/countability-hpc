# COCA Queries: Functional Anchoring Table Expansion

Task #3 from reviewer feedback. Current Table 5 has 3 pairs; need 8-10.

## Existing pairs (already in table)

| Quasi-count | Freq | three/M | Singulative | Freq | three/M | Ratio |
|---|---|---|---|---|---|---|
| police | 220,858 | 91 | officers | 60,161 | 3,956 | 44x |
| poultry | 4,544 | 220 | chickens | 8,745 | 3,431 | 16x |
| clergy | 5,879 | 510 | priests | 12,168 | 2,876 | 6x |

## New pairs to query

For each pair, I need:
1. **Total COCA frequency** of each noun
2. **`three [noun]` count** — head uses only (filter out modifier uses for quasi-count nouns that modify freely, e.g., *three cattle ranchers*)
3. Compute **three/M** = (three N count / noun freq) * 1,000,000

### Pair 4: cattle / cows

Already discussed in text but not in the table. Partial data exists:
- cattle: freq 14,376; three cattle = 7 head uses (from Table 1)
- **Need:** cows total freq, three cows count

Query: `three cows` (should be clean — *cows* doesn't function as a modifier)

### Pair 5: livestock / animals

- **Need:** livestock total freq (have: 6,982 from Table 3), three livestock count (have: 1 from Table 3; filter modifier uses)
- **Need:** animals total freq, three animals count

Query: `three animals` (clean — *animals* doesn't modify productively)

### Pair 6: vermin / rats

- **Need:** vermin total freq (have: 1,041 from Table 3), three vermin count (have: 0 from Table 3)
- **Need:** rats total freq, three rats count

Query: `three rats`

### Pair 7: youth / teenagers

- **Need:** youth total freq (have: 49,846 from Table 3), three youth count (have: 10 from Table 3; some may be the fully count sense "a youth")
- **Need:** teenagers total freq, three teenagers count

Query: `three teenagers`

### Pair 8: folks / ? (unanchored control)

This is the negative case: *folks* has no functional singulative. *Person* is semantically distinct (neutral, not in-group). Include to show the prediction: unanchored quasi-count nouns should be unstable.

- folks: freq 65,895; three folks = 17 (from Table 1)
- **Need:** Confirm there's no singulative. Could pair with *person* as a non-anchoring comparator, but the point is the absence of anchoring.

**Alternative framing:** Instead of a ratio, mark this row as "no singulative" to show the asymmetry.

## Optional additional pairs

### Pair 9: gentry / gentlemen (historical)

Might be too low-frequency in COCA to be useful. Check:
- **Need:** gentry total freq, three gentry count
- **Need:** gentlemen total freq, three gentlemen count

### Pair 10: personnel / employees

- **Need:** personnel total freq, three personnel count
- **Need:** employees total freq, three employees count

## Summary of queries needed

| Query | Notes |
|---|---|
| `cows` total freq | For cattle/cows pair |
| `three cows` | Should be clean |
| `animals` total freq | For livestock/animals pair |
| `three animals` | Should be clean |
| `rats` total freq | For vermin/rats pair |
| `three rats` | Should be clean |
| `teenagers` total freq | For youth/teenagers pair |
| `three teenagers` | Should be clean |
| `gentry` total freq | Optional |
| `three gentry` | Optional |
| `gentlemen` total freq | Optional |
| `three gentlemen` | Optional |
| `personnel` total freq | Optional |
| `three personnel` | Optional |
| `employees` total freq | Optional |
| `three employees` | Optional |
