# Statistical Analysis of CF Digits of $\pi$
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)

Large scale statistical analysis of the randomness of the continued fraction digits on $\pi$


## INSTALL 
1. Clone this repo

First we will clone this repo and set up a virtual environment nad download all the required packages.

```
git clone https://github.com/akhatua2/pi_cf_digits_statistics.git
cd pi_cf_digits_statistics
python3 -m venv igl_venv
source igl_venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

2. Download the data

Since the raw and processed data is very large for github here is the google drive link where you can download the data from. Please down this and move the `data` and `raw_data` folders into the `pi_cf_digits_statistics` folder. For running the provided scripts you only need the `data` folder. Please see in Misc section for how to convert the `raw_data` into the processed format.

Google Drive link - 
```
https://drive.google.com/drive/folders/1C7-0ixzZUMBNtBLvP6AvTjj2qstHGARq?usp=sharing
```

## Chi-Square Test on CF digits of $\pi$

The results from the runs in the following table are in the `results` folder. To run this test yourself 

```
python chi_square_test.py 
```

Use the `--help` flag to see the input parameters.

|Number of digits|Number of blocks|Number of groups|KS-test on Chi-Square Vals|
|--|--|--|--|
|30B|30K|10|0.418|
|30B|30K|50|0.470|
|1B|10K|10|0.414|
|1B|10K|50|0.184|
|1B|1K|10|0.077|
|1B|1K|50|0.840|
|10M|10|10|0.8053|
|10M|10|50|0.6403|
|10M|100|10|0.8657|
|10M|100|50|0.1637|
|100M|1K|10|0.1165|
|100M|1K|50|0.3459|
|100M|100|10|0.1819|
|100M|100|50|0.5548|

TODO:

Optimal values -> 10, 50 - groups, 10M, **1M**, 100K - blocksize (6 total runs)

## Chi-Square-Pairs Test on CF digits of $\pi$

The results from the runs in the following table are in the `results` folder. To run this test yourself 

```
python chi_square_pairs_test.py 
```

Use the `--help` flag to see the input parameters.

|Number of digits|Number of blocks|Number of pairs|KS-test on Chi-Square Vals|
|--|--|--|--|
|1B|1K|5|3.1474e-8|
|1B|10K|5|4.2490e-74|
|10M|10|5|0.8372|
|10M|10|5|0.0020|
|100M|1K|5|4.9684e-11|
|100M|100|5|0.1267|

TODO:

Optimal values -> 10, 50 - groups, 10M, **1M**, 100K - blocksize (6 total runs)

## Random and Pi Walk Tests on CF digits of $\pi$

To run this test for random walks mod 4
```
python walk.py --use_rand True --mod 4
```
To run this test for random walks mod 6
```
python walk.py --use_rand True --mod 6
```
To run this test for pi walks mod 4
```
python walk.py --mod 4
```
To run this test for pi walks mod 6
```
python walk.py --mod 6
```

|Number of digits|Number of blocks|Type or digits|Mod|MinMax|Mean|Variance|
|--|--|--|--|--|--|--|
|30M|1K|Random_1|4|(12971844.338, 103153685.155)|40769453.987|210973198162334.23|
|30M|1K|Random_2|4|(12876544.325, 108576945.287)|40586421.642|208297314523442.82|
|30M|1K|$\pi$   |4|(12832847.898, 110378456.214)|40659703.784|208373904890053.84|
|100K|1K|Random|4|(0.525, 5.208)|1.771|0.537|
|100K|1K|$\pi$ |4|(0.562, 4.682)|1.746|0.513|
|100K|1K|Random|6|(0.869, 7.718)|3.014|1.118|
|100K|1K|$\pi$ |6|(0.878, 8.388)|2.988|1.206|

## Random and Pi Sites visited Tests on CF digits of $\pi$

To run this test for random walks mod 4
```
python sites_visited.py --use_rand True --mod 4
```
To run this test for random walks mod 6
```
python sites_visited.py --use_rand True --mod 6
```
To run this test for pi walks mod 4
```
python sites_visited.py --mod 4
```
To run this test for pi walks mod 6
```
python sites_visited.py --mod 6
```

|Number of digits|Number of blocks|Type or digits|Mod|MinMax|Mean|Variance|Std Dev|Runtime|
|--|--|--|--|--|--|--|--|--|
|30M|1000|Random_1|4|(23045836, 25101953)|24318792.021|119744160752.9294|346040.692|16hrs|
|30M|1000|Random_2|4|(21384756, 24987201)|24128376.236|137956343984.6548|371424.748|16hrs|
|30M|1000|$\pi$   |4|(22725453, 25109780)|24280608.064|148322090202.4152|385126.070|18hrs|
|30M|1000|Random_1|6|(28237148, 29019277)|29623879.345|350466.2355|592.001|18hrs|
|30M|1000|Random_2|6|(29465349, 29129376)|29821463.987|357655.1923|598.042|18hrs|
|30M|1000|$\pi$   |6|(29744353, 29748462)|29746267.162|379760.6432|616.247|20hrs|
|100K|1K|Random|4|(90854, 176387)|147905.047|134260828.4412|11587.097|-|
|100K|1K|$\pi$|4|(97143, 172690)|146080.107|137343287.3529|11719.3552|-|
|100K|1K|Random|6|(17784, 21548)|20094.057|207318.9787|455.322|-|
|100K|1K|$\pi$|6|(17880, 21135)|19854.228|193608.8428|440.0100|-|

##  Cut-off value on CF digits of $\pi$


|Number of digits|Cut-of number(m)|Blocksize(n)|Theoretical value(Pr_T)|Experimental value(Pr_E)|Difference|
|--|--|--|--|--|--|
|10M|600|1000|0.9097688732593405|0.907|-0.0027688732593404985|
|10M|1000|1000|0.7637854600148878|0.7666|0.0028145399851121633|
|10M|2000|1000|0.513942043357302|0.5132|-0.0007420433573019913|
|10M|5000|1000|0.25065200098279206|0.2507|4.79990172079225e-05|
|10M|10000|1000|0.1343483455185307|0.136|0.0016516544814693113|
|10M|100000|10000|0.13434585722629822|0.128|-0.006345857226298213|
|10M|1000000|10000|0.01432338377020792|0.02|0.00567661622979208|
|10M|10000000|10000|0.0014416548888593894|0.001|-0.0004416548888593894|
|100M|10000|1000|0.1343483455185307|0.13569|0.0013416544814693065|
|100M|100000|1000|0.014323412100246347|0.01449|0.00016658789975365282|
|100M|1000000|1000|0.0014416551754701246|0.00169|0.00024834482452987553|

##  Extreme value statistics of $\pi$ for Quartiles in Max_Digits

|Number of digits|Blocksize(n)|Quartiles(1-Pr)|Experimental value(m_E)|Theoretical value(m_T)|
|--|--|--|--|--|
|10M|100|10%|63|62.6554495327263|
|10M|100|25%|104|104.06844905028039|
|10M|100|50%|208|208.13689810056078|
|10M|100|75%|501|501.48937978426767|
|10M|100|90%|1377|1369.2938306930143|
|10M|1000|10%|620|626.554495327263|
|10M|1000|25%|1046|1040.684490502804|
|10M|1000|50%|2072|2081.368981005608|
|10M|1000|75%|5016|5014.893797842677|
|10M|1000|90%|13460|13692.938306930142|
|10M|10000|10%|6090|6265.54495327263|
|10M|10000|25%|10479|10406.84490502804|
|10M|10000|50%|20311|20813.68981005608|
|10M|10000|75%|49379|50148.937978426766|
|10M|10000|90%|126163|136929.38306930143|
|100M|100|10%|63|62.6554495327263|
|100M|100|25%|104|104.0684490502803|
|100M|100|50%|208|208.13689810056078|
|100M|100|75%|502|501.48937978426767|
|100M|100|90%|1372|1369.2938306930143|
|100M|1000|10%|628|626.554495327263|
|100M|1000|25%|1044|1040.684490502804|
|100M|1000|50%|2081|2081.368981005608|
|100M|1000|75%|5037|5014.893797842677|
|100M|1000|90%|13818|13692.938306930142|
|100M|10000|10%|6444|6265.54495327263|
|100M|10000|25%|10654|10406.84490502804|
|100M|10000|50%|20970|20813.68981005608|
|100M|10000|75%|51469|50148.937978426766|
|100M|10000|90%|135329|136929.38306930143|












