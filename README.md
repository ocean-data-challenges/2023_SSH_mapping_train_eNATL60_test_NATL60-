# 2023_SSH_mapping_train_eNATL60_test_NATL60

> [!NOTE]
> This repository is still under construction, changes are likely to occur.


## Motivation

This datachallenge is based on the principle of the [SSH Mapping Data Challenge 2020a](https://github.com/ocean-data-challenges/2020a_SSH_mapping_NATL60). The aim is again to compare several methods for reconstructing sequences of Sea Surface Height (SSH) from partial satellite altimeter observations. As in the previous datachallenge, this datachallenge follows the framework of an OSSE (Observation System Simulation Experiment) where "Real" full SSH are from a numerical simulation with a realistic, high-resolution ocean circulation model: the reference simulation. However, this datachallenge proposes to use two separate reference simulations, each covering an entire year, whereas previous datachallenges only used a single simulation covering one year: a first simulation for training methods requiring learning from full SSH fields, and a second for evaluating different reconstruction methods over a full year. On the one hand, this approach enables a longer learning period: a whole year, whereas in previous data challenges, learning was limited to a few months to maintain an independent evaluation period within the same year. Secondly, SSH reconstructions can be validated on a full year of data, totally independent of the learning data, making it possible to study any seasonal effects in reconstruction performance.

## Design of experiment

### Reference simulations

The two references simulations used are the **NATL60-CJM165** and the **eNATL60-BLB002** simulations, both based on the NEMO model, tide-free, and with a nature run grid resolution of 1/60°.
- **NATL60-CJM165** covers the North Atlantic region, and provides hourly output data. For more detailed information, please visit this link: [NATL60-CJM165 Information](https://github.com/meom-configurations/NATL60-CJM165).
- **eNATL60-BLB002**: This simulation covers an extended area, including the tropical/equatorial Atlantic, the entire Mediterranean Sea, and the Black Sea. It offers a more realistic simulation, including surface pressure forcing, but it does not have the explicit resolution of tides. The nature run grid resolution is 1/60° with hourly output. You can find additional information at this link: [eNATL60 Information](https://github.com/ocean-next/eNATL60).

For convenience and memory consideration, we have reinterpolated both of these simulations onto two different grid resolutions: **1/20°** and **1/8°**. Additionally, we have provided **daily mean resampling** for these datasets.

### Observations

The SSH observations include simulations of seven altimeters data: Jason-3, Sentinel-3a, Sentinel-3b, Cryosat-2, Saral/Altika, Haiyang-2a, Haiyang-2b. This nadir altimeters constellation was operating during the 2019-2020 period. No observation error is considered in this challenge.

### Data sequence and use

The reconstruction of the SSH is evaluated on the **NATL60** domain over the whole year; however, 20 days are cropped at the beginning and at the end of this period for methods which might suffer from side effets. Therefore, the actual evaluation period (from which the metrics are computed) starts the 2012-10-21 and ends the 2013-09-10.

For reconstruction methods that require learning from complete SSH fields, training is carried out on the **eNATL60** domain over the whole year, which corresponds to the period from 2009-07-01 to 2010-06-30. The validation subset can be chosen from the latter.

<img src='figures/periods_enatl_natl.png' alt='Periods eNATL NATL diagram'>

Sub-periods are also considered for the evaluation: 40 days are chosen in the
middle of each season:

<img src='figures/sub_periods_seasons.png' alt='Sub-periods NATL diagram'>


### Domains for evaluation

As we waim to evaluate the reconstruction performance of the different mapping methods at the scale of the North Atlantic basin, we define 3 different regions for the calculation of reconstruction metrics. The selected regions show strong disparities in terms of ocean variability, but also in terms of spatial coverage by the altimeter constellation due to their different latitudes. They seem a good choice for estimating the performance of the mapping methods in various situations in the North Atlantic basin.

- **GF** : **[64°O x 49°O , 29°N x 44°N]**
- **GRE** : **[39°O x 24°O , 49°N x 64°N]**
- **MAD** : **[27°O x 12°O , 29°N x 44°N]**


<img src='figures/evaluation_domains.png' alt='evaluation domains : GF, GRE, MAD, CAV'>

## Leaderboard

Click on one of the period below to show the scores associated to each method on
each region.

In the tables below, denominations like "**4DVarNet-GF 1/20°**" mean the model was trained using the 4DVarNet method on the region of GF at a resolution of 1/20°.

The considered metrics are:
- µ(RMSE): average RMSE score (the closer to 1, the better)
- σ(RMSE): standard deviation of the RMSE score;
- λx (°): minimum spatial scale resolved (the closer to 0, the better);
- λt (days): minimum temporal scale resolved (the closer to 0, the better).

<details>

  <summary>Whole year</summary>

  **Evaluation on GF**:
  | Method                 | µ(RMSE) | σ(RMSE) | λx (°) | λt (days) | Reference |
  | ---------------------- | ------- | ------- | ------ | --------- | --------- |
  | MIOST                  | 0.926   | 0.011   | 1.315  | 13.39     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_miost.ipynb) |
  | 4DVarNet-GF 1/20° | 0.960   | 0.007   | 0.805  |  5.166    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_20_GF_7nad.ipynb) |
  | 4DVarNet-GF 1/8°  | 0.959   | 0.006   | 0.852  |  5.108    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GF_7nad.ipynb) |
  | 4DVarNet-GRE 1/8° | 0.933   | 0.011   | 1.049  |  5.791    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GRE_7nad.ipynb) |
  | 4DVarNet-MAD 1/8° | 0.931   | 0.01    | 1.075  |  3.721    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_MAD_7nad.ipynb) |

  **Evaluation on GRE**:
  | Method                 | µ(RMSE) | σ(RMSE) | λx (°) | λt (days) | Reference |
  | ---------------------- | ------- | ------- | ------ | --------- | --------- |
  | MIOST                  | 0.956   | 0.006   | 1.112  | 15.5      | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_miost.ipynb) |
  | 4DVarNet-GF 1/20° | 0.954   | 0.008   | 1.029  |  6.579    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_20_GF_7nad.ipynb) |
  | 4DVarNet-GF 1/8°  | 0.953   | 0.007   | 1.038  |  5.644    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GF_7nad.ipynb) |
  | 4DVarNet-GRE 1/8° | 0.972   | 0.005   | 0.804  |  2.62     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GRE_7nad.ipynb) |
  | 4DVarNet-MAD 1/8° | 0.964   | 0.006   | 0.891  |  3.312    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_MAD_7nad.ipynb) |

  **Evaluation on MAD**:
  | Method                 | µ(RMSE) | σ(RMSE) | λx (°) | λt (days) | Reference |
  | ---------------------- | ------- | ------- | ------ | --------- | --------- |
  | MIOST                  | 0.951   | 0.008   | 0.926  | 21.93     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_miost.ipynb) |
  | 4DVarNet-GF 1/20° | 0.952   | 0.01    | 0.91   |  6.616    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_20_GF_7nad.ipynb) |
  | 4DVarNet-GF 1/8°  | 0.951   | 0.009   | 0.937  |  5.705    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GF_7nad.ipynb) |
  | 4DVarNet-GRE 1/8° | 0.965   | 0.007   | 0.821  |  2.566    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GRE_7nad.ipynb) |
  | 4DVarNet-MAD 1/8° | 0.971   | 0.006   | 0.72   |  3.308    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_MAD_7nad.ipynb) |

</details>

<details>

  <summary>Mid Autumn</summary>

  **Evaluation on GF**:
  | Method                 | µ(RMSE) | σ(RMSE) | λx (°) | λt (days) | Reference |
  | ---------------------- | ------- | ------- | ------ | --------- | --------- |
  | MIOST                  | 0.941   | 0.008   | 1.367  | 10.22     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_miost.ipynb) |
  | 4DVarNet-GF 1/20° | 0.970   | 0.004   | 0.712  | 5.009     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_20_GF_7nad.ipynb) |
  | 4DVarNet-GF 1/8°  | 0.967   | 0.005   | 0.749  | 4.77      | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GF_7nad.ipynb) |
  | 4DVarNet-GRE 1/8° | 0.944   | 0.01    | 1.179  | 7.952     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GRE_7nad.ipynb) |
  | 4DVarNet-MAD 1/8° | 0.945   | 0.006   | 1.345  | 9.438     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_MAD_7nad.ipynb) |

  **Evaluation on GRE**:
  | Method                 | µ(RMSE) | σ(RMSE) | λx (°) | λt (days) | Reference |
  | ---------------------- | ------- | ------- | ------ | --------- | --------- |
  | MIOST                  | 0.958   | 0.005   | 1.392  | 6.36      | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_miost.ipynb) |
  | 4DVarNet-GF 1/20° | 0.956   | 0.007   | 1.185  | 5.99      | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_20_GF_7nad.ipynb) |
  | 4DVarNet-GF 1/8°  | 0.956   | 0.006   | 1.177  | 5.64      | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GF_7nad.ipynb) |
  | 4DVarNet-GRE 1/8° | 0.975   | 0.004   | 0.823  | 2.714     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GRE_7nad.ipynb) |
  | 4DVarNet-MAD 1/8° | 0.967   | 0.004   | 0.911  | 3.481     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_MAD_7nad.ipynb) |

  **Evaluation on MAD**:
  | Method                 | µ(RMSE) | σ(RMSE) | λx (°) | λt (days) | Reference |
  | ---------------------- | ------- | ------- | ------ | --------- | --------- |
  | MIOST                  | 0.952   | 0.006   | 1.229  | 4.4       | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_miost.ipynb) |
  | 4DVarNet-GF 1/20° | 0.949   | 0.011   | 1.138  | 6.935     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_20_GF_7nad.ipynb) |
  | 4DVarNet-GF 1/8°  | 0.950   | 0.010   | 1.128  | 5.674     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GF_7nad.ipynb) |
  | 4DVarNet-GRE 1/8° | 0.965   | 0.007   | 1.002  | 3.416     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GRE_7nad.ipynb) |
  | 4DVarNet-MAD 1/8° | 0.971   | 0.007   | 0.866  | 3.346     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_MAD_7nad.ipynb) |

</details>

<details>

  <summary>Mid Winter</summary>

  **Evaluation on GF**:
  | Method                 | µ(RMSE) | σ(RMSE) | λx (°) | λt (days) | Reference |
  | ---------------------- | ------- | ------- | ------ | --------- | --------- |
  | MIOST                  | 0.926   | 0.007   | 1.425  | 8.15      | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_miost.ipynb) |
  | 4DVarNet-GF 1/20° | 0.957   | 0.005   | 0.913  | 5.69      | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_20_GF_7nad.ipynb) |
  | 4DVarNet-GF 1/8°  | 0.957   | 0.004   | 0.894  | 5.31      | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GF_7nad.ipynb) |
  | 4DVarNet-GRE 1/8° | 0.934   | 0.008   | 1.172  | 7.15      | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GRE_7nad.ipynb) |
  | 4DVarNet-MAD 1/8° | 0.931   | 0.008   | 1.342  | 6.878     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_MAD_7nad.ipynb) |

  **Evaluation on GRE**:
  | Method                 | µ(RMSE) | σ(RMSE) | λx (°) | λt (days) | Reference |
  | ---------------------- | ------- | ------- | ------ | --------- | --------- |
  | MIOST                  | 0.953   | 0.006   | 1.312  | 11.01     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_miost.ipynb) |
  | 4DVarNet-GF 1/20° | 0.948   | 0.007   | 1.177  | 7.268     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_20_GF_7nad.ipynb) |
  | 4DVarNet-GF 1/8°  | 0.948   | 0.007   | 1.177  | 6.948     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GF_7nad.ipynb) |
  | 4DVarNet-GRE 1/8° | 0.969   | 0.005   | 0.828  | 2.595     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GRE_7nad.ipynb) |
  | 4DVarNet-MAD 1/8° | 0.961   | 0.006   | 1.084  | 3.221     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_MAD_7nad.ipynb) |

  **Evaluation on MAD**:
  | Method                 | µ(RMSE) | σ(RMSE) | λx (°) | λt (days) | Reference |
  | ---------------------- | ------- | ------- | ------ | --------- | --------- |
  | MIOST                  | 0.943   | 0.006   | 1.209  | 4.72      | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_miost.ipynb) |
  | 4DVarNet-GF 1/20° | 0.943   | 0.008   | 1.073  | 6.27      | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_20_GF_7nad.ipynb) |
  | 4DVarNet-GF 1/8°  | 0.942   | 0.007   | 1.041  | 5.39      | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GF_7nad.ipynb) |
  | 4DVarNet-GRE 1/8° | 0.959   | 0.005   | 0.876  | 2.861     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GRE_7nad.ipynb) |
  | 4DVarNet-MAD 1/8° | 0.966   | 0.005   | 0.807  | 3.759     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_MAD_7nad.ipynb) |

</details>

<details>

  <summary>Mid Spring</summary>

  **Evaluation on GF**:
  | Method                 | µ(RMSE) | σ(RMSE) | λx (°) | λt (days) | Reference |
  | ---------------------- | ------- | ------- | ------ | --------- | --------- |
  | MIOST                  | 0.921   | 0.011   | 1.324  | 10.44     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_miost.ipynb) |
  | 4DVarNet-GF 1/20° | 0.955   | 0.008   | 0.839  |  6.549    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_20_GF_7nad.ipynb) |
  | 4DVarNet-GF 1/8°  | 0.955   | 0.006   | 0.911  |  5.74     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GF_7nad.ipynb) |
  | 4DVarNet-GRE 1/8° | 0.927   | 0.011   | 1.049  |  7.78     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GRE_7nad.ipynb) |
  | 4DVarNet-MAD 1/8° | 0.927   | 0.007   | 1.139  | 10.719    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_MAD_7nad.ipynb) |

  **Evaluation on GRE**:
  | Method                 | µ(RMSE) | σ(RMSE) | λx (°) | λt (days) | Reference |
  | ---------------------- | ------- | ------- | ------ | --------- | --------- |
  | MIOST                  | 0.958   | 0.002   | 1.269  | 12.24     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_miost.ipynb) |
  | 4DVarNet-GF 1/20° | 0.958   | 0.002   | 0.995  | 5.839     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_20_GF_7nad.ipynb) |
  | 4DVarNet-GF 1/8°  | 0.956   | 0.002   | 0.964  | 5.257     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GF_7nad.ipynb) |
  | 4DVarNet-GRE 1/8° | 0.974   | 0.002   | 0.775  | 2.612     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GRE_7nad.ipynb) |
  | 4DVarNet-MAD 1/8° | 0.967   | 0.002   | 0.964  | 3.321     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_MAD_7nad.ipynb) |

  **Evaluation on MAD**:
  | Method                 | µ(RMSE) | σ(RMSE) | λx (°) | λt (days) | Reference |
  | ---------------------- | ------- | ------- | ------ | --------- | --------- |
  | MIOST                  | 0.951   | 0.003   | 1.138  | 17.65     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_miost.ipynb) |
  | 4DVarNet-GF 1/20° | 0.954   | 0.004   | 0.832  | 13.83     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_20_GF_7nad.ipynb) |
  | 4DVarNet-GF 1/8°  | 0.952   | 0.003   | 0.97   |  5.742    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GF_7nad.ipynb) |
  | 4DVarNet-GRE 1/8° | 0.966   | 0.003   | 0.832  | 3.27      | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GRE_7nad.ipynb) |
  | 4DVarNet-MAD 1/8° | 0.971   | 0.001   | 0.78   | 3.365     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_MAD_7nad.ipynb) |

</details>

<details>

  <summary>Mid Summer</summary>

  **Evaluation on GF**:
  | Method                 | µ(RMSE) | σ(RMSE) | λx (°) | λt (days) | Reference |
  | ---------------------- | ------- | ------- | ------ | --------- | --------- |
  | MIOST                  | 0.923   | 0.007   | 1.575  | 10.04     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_miost.ipynb) |
  | 4DVarNet-GF 1/20° | 0.958   | 0.005   | 0.648  | 5.56      | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_20_GF_7nad.ipynb) |
  | 4DVarNet-GF 1/8°  | 0.956   | 0.004   | 0.929  | 5.56      | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GF_7nad.ipynb) |
  | 4DVarNet-GRE 1/8° | 0.928   | 0.007   | 0.937  | 8.723     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GRE_7nad.ipynb) |
  | 4DVarNet-MAD 1/8° | 0.923   | 0.006   | 1.066  | 10.076    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_MAD_7nad.ipynb) |

  **Evaluation on GRE**:

  | Method                 | µ(RMSE) | σ(RMSE) | λx (°) | λt (days) | Reference |
  | ---------------------- | ------- | ------- | ------ | --------- | --------- |
  | MIOST                  | 0.963   | 0.002   | 1.227  | 13.09     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_miost.ipynb) |
  | 4DVarNet-GF 1/20° | 0.961   | 0.003   | 1.061  |  9.484    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_20_GF_7nad.ipynb) |
  | 4DVarNet-GF 1/8°  | 0.958   | 0.002   | 1.05   |  6.54     | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GF_7nad.ipynb) |
  | 4DVarNet-GRE 1/8° | 0.977   | 0.001   | 0.75   |  2.559    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GRE_7nad.ipynb) |
  | 4DVarNet-MAD 1/8° | 0.97    | 0.002   | 0.876  |  3.494    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_MAD_7nad.ipynb) |

  **Evaluation on MAD**:

  | Method                 | µ(RMSE) | σ(RMSE) | λx (°) | λt (days) | Reference |
  | ---------------------- | ------- | ------- | ------ | --------- | --------- |
  | MIOST                  | 0.96    | 0.002   | 1.346  | 12.7      | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_miost.ipynb) |
  | 4DVarNet-GF 1/20° | 0.962   | 0.003   | 0.956  | 14.959    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_20_GF_7nad.ipynb) |
  | 4DVarNet-GF 1/8°  | 0.96    | 0.003   | 1.001  |  6.695    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GF_7nad.ipynb) |
  | 4DVarNet-GRE 1/8° | 0.97    | 0.004   | 0.961  |  3.909    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_GRE_7nad.ipynb) |
  | 4DVarNet-MAD 1/8° | 0.977   | 0.002   | 0.782  |  3.668    | [link](https://github.com/ocean-data-challenges/2023_SSH_mapping_train_eNATL60_test_NATL60-/blob/main/notebooks/eval_4dvarnet_1_8_MAD_7nad.ipynb) |

</details>


## Data

### Data description
The data are available with the following repository structure:
```
|-- dc_ref
|   |-- eNATL60-BLB002-daily-reg-1_20.nc
|   |-- eNATL60-BLB002-daily-reg-1_8.nc
|   |-- NATL60-CJM165-daily-reg-1_20.nc
|   |-- NATL60-CJM165-daily-reg-1_8.nc
|-- dc_obs
|   |-- eNATL60-BLB002-alongtrack.gz
|   |-- NATL60-CJM165-alongtrack.gz
```
In the ```dc_ref``` repository, daily mean resampling of the reference simulations variables are provided for both **eNATL60-BLB002** and **NATL60-CJM165** : at the **1/8°** (```*-*-daily-reg-1_8.nc```) and the **1/20°** (```*-*-daily-reg-1_20.nc```) resolution grid.

In the ```dc_obs``` repository, the **alongtrack** files (```*-*-alongtrack.gz```) store the simulated SSH observations. For both **eNATL60-BLB002** and **NATL60-CJM165** simulations,  the variables are interpolated onto the **2019-2020 nadir altimeter constellation** available in CMEMS, i.e., Jason-3, Sentinel-3a, Sentinel-3b, Cryosat-2, Saral/Altika, Haiyang-2a, Haiyang-2b.

- For the **NATL60-CJM165** datasets, you will find the following variables:
  ```
  coordinates:
      lat: latitude vector [degree north]
      lon: longitude vector [degree east]
      time: time vector [date time]
  ```
  ```
  variables:
      ssh: sea surface height simulated by the model [meters]
      mdt: mean dynamic topography, computed as the temporal averaged simulated ssh [meters]
      ssh_variance: variance map of the ssh variable [meters²]
      sla: sea level anomaly, computed as: sla = ssh - mdt [meters]
      ssh_norm: normalized ssh (using fir 4dvarnet mapping), computed as: ssh_norm = sla/sqrt(ssh_variance) [no unit]
  ```

- For the **eNATL60-BLB002** dataset, you will find the following variables:
  ```
  coordinates:
      lat: latitude vector [degree north]
      lon: longitude vector [degree east]
      time: time vector [date time]
  ```
  ```
  variables:
      ssh_model_with_HF: sea surface height simulated by the model [meters]
      ssh: sea surface height simulated by the model without high frequency signal, i.e., with DAC ERA-INTERIM ssh signal removed and 25h temporal filtering to remove residual tidal effects [meters]
      mdt: mean dynamic topography, computed as the temporal averaged simulated ssh [meters]
      ssh_variance: variance map of the ssh variable [meters²]
      sla: sea level anomaly, computed as: sla = ssh - mdt [meters]
      ssh_norm: normalized ssh (using fir 4dvarnet mapping), computed as: ssh_norm = sla/sqrt(ssh_variance) [no unit]
  ```
### Download the data

The datasets of simulations daily mean resampling are available at the following links:
- **eNATL60-BLB002** (1/20°):
    ```
    https://s3.eu-central-1.wasabisys.com/melody/data_challenge_Daniel_Guillaume/public/dc_ref/eNATL60-BLB002-daily-reg-1_20.nc
    ```
- **eNATL60-BLB002** (1/8°):
    ```
    https://s3.eu-central-1.wasabisys.com/melody/data_challenge_Daniel_Guillaume/public/dc_ref/eNATL60-BLB002-daily-reg-1_8.nc
    ```
- **NATL60-CJM165** (1/20°) - *for evaluation*:
    ```
    https://s3.eu-central-1.wasabisys.com/melody/data_challenge_Daniel_Guillaume/public/dc_ref/NATL60-CJM165-daily-reg-1_20.nc
    ```
- **NATL60-CJM165** (1/8°) - *for evaluation*:
    ```
    https://s3.eu-central-1.wasabisys.com/melody/data_challenge_Daniel_Guillaume/public/dc_ref/NATL60-CJM165-daily-reg-1_8.nc
    ```

The alongtrack files are archived in zip format as they contain a lot of files. They are available at the following links:

- **eNATL60-BLB002 alongtracks**:
    ```
    https://s3.eu-central-1.wasabisys.com/melody/data_challenge_Daniel_Guillaume/public/dc_obs/eNATL60-BLB002-alongtrack.gz
    ```
- **NATL60-CJM165 alongtracks**:
    ```
    https://s3.eu-central-1.wasabisys.com/melody/data_challenge_Daniel_Guillaume/public/dc_obs/NATL60-CJM165-alongtrack.gz
    ```

To download a file, you can use the `wget` command. For example, if you want to download NATL60-CJM165 with a resolution of 1/8°:
```sh
wget https://s3.eu-central-1.wasabisys.com/melody/data_challenge_Daniel_Guillaume/public/dc_ref/NATL60-CJM165-daily-reg-1_8.nc
```
To extract an archive in the same directory, use the `tar` command. For example, if you want to download NATL60's alongtrack and extract it from its archive:
```sh
wget https://s3.eu-central-1.wasabisys.com/melody/data_challenge_Daniel_Guillaume/public/dc_obs/NATL60-CJM165-alongtrack.gz

tar -zxvf NATL60-CJM165-alongtrack.gz
```


### Prepare the data

For mapping methods that take as input **gridded observations** instead of raw along tracks, we provide a **binning** script ```alongtrack_binning.ipynb```, that interpolates simulated along tracks observations on a daily grid whose spatial resolution is left to the user's choice (1/8° or 1/20°).
