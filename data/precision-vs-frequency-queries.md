# Precision vs. Frequency Discriminating Test

## The question
Does the hierarchy reflect semantic precision or collocation frequency?

## The test
Find determinatives where frequency and precision dissociate.

### Queries needed

#### Base frequencies (determinatives)
    numerous
    various
    two
    each
    every

#### Low-frequency + semantically LOOSE (predict: accept quasi-count)
    numerous cattle
    numerous folks
    numerous people
    various cattle
    various folks
    various people

#### High-frequency + semantically TIGHT (predict: reject quasi-count)
    two cattle
    two folks
    two people
    each cattle
    each folks
    each people
    every cattle
    every folks
    every people

## Predictions

If **precision** drives the pattern:
- *numerous cattle* should work (loose, like *many cattle*)
- *two cattle* should fail (tight, like *three cattle*)
- regardless of determinative frequency

If **frequency** drives the pattern:
- *two cattle* should work BETTER than *three cattle* (because *two* is more frequent than *three*)
- *numerous cattle* should fail (because *numerous* is rare)
