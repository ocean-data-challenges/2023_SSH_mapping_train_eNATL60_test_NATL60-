# 2023_SSH_mapping_train_eNATL60_test_NATL60

### Data sequence and use

The reconstruction of the SSH is evaluated on the NATL60 domain over the whole year, which corresponds to the period from 2012-10-01 to 2013-09-30.

For reconstruction methods that require learning from complete SSH fields, training is carried out on the eNATL60 domain over the whole year, which corresponds to the period from 2009-07-01 to 2010-06-30. The validation subset can be chosen from the latter.

<img src='periods_enatl_natl.png' alt='Periods eNATL NATL diagram'>

<!-- TODO: parler des sous-périodes (milieux de saisons) -->


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
