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
|1B|1K|10|0.0414|
|1B|1K|50|0.0184|
|1B|1K|10|0.0077|
|1B|1K|50|0.0840|
|10M|10|10|0.8053|
|10M|10|50|0.6403|
|10M|100|10|0.8657|
|10M|100|50|0.1637|
|100M|1K|10|0.1165|
|100M|1K|50|0.3459|
|100M|100|10|0.1819|
|100M|100|50|0.5548|

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

|Number of digits|Number of runs|Mod|Type or digits|MinMax|Mean|Variance|
|--|--|--|--|--|--|--|
|1B|1K|Random|4|(0.5251, 5.2086)|1.7712|0.5376|
|1B|1K|$\pi$|4|(0.5619, 4.6821)|1.7467|0.5131|
|1B|1K|Random|6|(0.8699, 7.7178)|3.0139|1.1177|
|1B|1K|$\pi$|6|(1380.0823, 13175.6054)|4694.2315|2976212.7692|

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

|Number of digits|Number of runs|Mod|Type or digits|MinMax|Mean|Variance|
|--|--|--|--|--|--|--|
|1B|1K|Random|4|(90854, 176387)|147905.047|134260828.4412|
|1B|1K|$\pi$|4|(97143, 172690)|146080.107|137343287.3529|
|1B|1K|Random|6|(17784, 21548)|20094.057|207318.9787|
|1B|1K|$\pi$|6|(17880, 21135)|19854.228|193608.8428|



