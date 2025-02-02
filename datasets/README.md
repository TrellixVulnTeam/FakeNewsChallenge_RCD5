https://github.com/FakeNewsChallenge/fnc-1

# Stance Detection dataset for FNC-1

For details of the task, see [FakeNewsChallenge.org](http://fakenewschallenge.org)


The data provided is `(headline, body, stance)` instances, where `stance` is one of `{unrelated, discuss, agree, disagree}`. The dataset is provided as two CSVs:


### `train_bodies.csv`

This file contains the body text of articles (the `articleBody` column) with corresponding IDs (`Body ID`)

### `train_stances.csv`

This file contains the labeled stances (the `Stance` column) for pairs of article headlines (`Headline`) and article bodies (`Body ID`, referring to entries in `train_bodies.csv`).

### Distribution of the data

The distribution of `Stance` classes in `train_stances.csv` is as follows:

|   rows |   unrelated |   discuss |     agree |   disagree |
|-------:|------------:|----------:|----------:|-----------:|
|  49972 |    0.73131  |  0.17828  | 0.0736012 |  0.0168094 |

Credits:

- Edward Misback
- Craig Pfeifer

Note:
- `test_bodies.csv` and `test_stances_unlabeled.csv` were released 2 weeks before the submission date - the actual articles to be used for evaluating the submissions, but without the labels.
- `competition_test_bodies.csv`, `competition_test_stances.csv` and `competition_test_stances_unlabeled.csv` contain the actual data used in the final evaluation of the contestants' submissions (same as test_* but with labels).
