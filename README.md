# 2023_SSH_mapping_train_eNATL60_test_NATL60

### Data sequence and use

The reconstruction of the SSH is evaluated on the **NATL60** domain over the whole year, which corresponds to the period from 2012-10-01 to 2013-09-30.

For reconstruction methods that require learning from complete SSH fields, training is carried out on the **eNATL60** domain over the whole year, which corresponds to the period from 2009-07-01 to 2010-06-30. The validation subset can be chosen from the latter.

<img src='figures/periods_enatl_natl.png' alt='Periods eNATL NATL diagram'>

Sub-periods are also considered for the evaluation: 40 days are chosen in the
middle of each season:

<img src='figures/sub_periods_seasons.png' alt='Sub-periods NATL diagram'>

<!--
To highlight the particularities of the different seasons of the year, sub-periods of 40 days in the middle of each season are defined. In this situation, for learning-based methods, training on the X sub-periods of eNATL60 would naturally lead to the assessment of the model on X sub-periods of NATL60 or the whole domain

TODO: parler des sous-périodes (milieux de saisons)

- Hiver     : YYYY-02-01 à YYYY-03-13
- Printemps : YYYY-04-30 à YYYY-06-09
- Été       : YYYY-07-11 à YYYY-08-20
- Automne   : YYYY-10-21 à YYYY-11-30
-->


## Leaderboard

| Method | µ(RMSE) | σ(RMSE) | λx (°) | λt (days) | Notes | Reference |
| ------ | ------- | ------- | ------ | --------- | ----- | --------- |
| MIOST  | . | . | . | . | . | . |
| 4DVarNet-NATL  | . | . | . | . | . | . |
| 4DVarNet-GF  | . | . | . | . | . | . |
| etc  | . | . | . | . | . | . |

With:
- µ(RMSE): average RMSE score;
- σ(RMSE): standard deviation of the RMSE score;
- λx: minimum spatial scale resolved;
- λt: minimum temporal scale resolved.
