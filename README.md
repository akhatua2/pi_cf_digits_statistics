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
|1B|10K|10|0.0414|
|1B|10K|50|0.0184|
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

|Number of digits|Number of runs|Type or digits|Mod|MinMax|Mean|Variance|
|--|--|--|--|--|--|--|
|1B|1K|Random|4|(0.525, 5.208)|1.771|0.537|
|1B|1K|$\pi$|4|(0.562, 4.682)|1.746|0.513|
|1B|1K|Random|6|(0.869, 7.718)|3.014|1.118|
|1B|1K|$\pi$|6|(0.878, 8.388)|2.988|1.206|

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

|Number of digits|Number of runs|Mod|Type or digits|MinMax|Mean|Variance|Std Dev|
|--|--|--|--|--|--|--|--|
|1B|1K|Random|4|(90854, 176387)|147905.047|134260828.4412|11587.097|
|1B|1K|$\pi$|4|(97143, 172690)|146080.107|137343287.3529|11719.3552|
|1B|1K|Random|6|(17784, 21548)|20094.057|207318.9787|455.322|
|1B|1K|$\pi$|6|(17880, 21135)|19854.228|193608.8428|440.0100|

##  Cut-off value on CF digits of $\pi$


|Number of digits|Cut-of number|Blocksize|Theoretical value|Experimental value|Difference|
|--|--|--|--|--|--|
|10M|10000|1000|0.1343483455185307|0.136|0.0016516544814693113|
|10M|100000|1000|0.014323412100246347|0.0135|-0.0008234121002463467|
|10M|1000000|1000|0.0014416551754701246|0.002|0.0005583448245298755|
|10M|100000|10000|0.13434585722629822|0.128|-0.006345857226298213|
|10M|1000000|10000|0.01432338377020792|0.02|0.00567661622979208|
|10M|10000000|10000|0.0014416548888593894|0.001|-0.0004416548888593894|
|100M|10000|1000|0.1343483455185307|0.13569|0.0013416544814693065|
|100M|100000|1000|0.014323412100246347|0.01449|0.00016658789975365282|
|100M|1000000|1000|0.0014416551754701246|0.00169|0.00024834482452987553|





