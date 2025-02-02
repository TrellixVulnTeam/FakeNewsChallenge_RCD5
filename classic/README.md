# Our solution
Based on the Baseline FNC implementation https://github.com/FakeNewsChallenge/fnc-1-baseline

The features are similar, but the classification pipeline is heavily modified

## 2-stage over TEST

First stage results:

|           |  related  | unrelated |
| --------- | --------- | --------- |
|  related  |   6382    |    682    |
| unrelated |    379    |   17970   |

Score: 6088.0 out of 6353.25    (95.82497147129422%)

Both stages:

|           |   agree   | disagree  |  discuss  | unrelated |
| --------- | --------- | --------- | --------- | --------- |
|   agree   |    109    |     0     |   1637    |    157    |
| disagree  |    16     |     0     |    529    |    152    |
|  discuss  |    89     |     0     |   4002    |    373    |
| unrelated |     1     |     0     |    378    |   17970   |

Score: 9171.25 out of 11651.25  (78.71473017916533%)

## 1-stage over TEST

|           |   agree   | disagree  |  discuss  | unrelated |
| --------- | --------- | --------- | --------- | --------- |
|   agree   |    98     |     2     |   1590    |    213    |
| disagree  |    14     |     1     |    488    |    194    |
|  discuss  |    116    |     2     |   3838    |    508    |
| unrelated |     2     |     0     |    243    |   18104   |

Score: 9016.0 out of 11651.25   (77.3822551228409%)

## 1-stage over train (10-fold cross-validation)

Score for fold 8 = 0.8046619554899272   
Score for fold 5 = 0.7986692669496387   
Score for fold 0 = 0.8156965600726319   
Score for fold 4 = 0.8055000587613116   
Score for fold 6 = 0.8125525651808242   
Score for fold 2 = 0.8409216183441738   
Score for fold 7 = 0.8182117028270874   
Score for fold 9 = 0.8078912546613738   
Score for fold 3 = 0.8063854047890536   
Score for fold 1 = 0.8238887003732609   
Average score 0.8134379087449283   
