# Statistical Analysis of CF Digits of Pi
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)

Large scale statistical analysis of the randomness of the continued fraction digits on pi


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

## Chi-Square Test on CF digits of Pi

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

## Chi-Square-Pairs Test on CF digits of Pi

The results from the runs in the following table are in the `results` folder. To run this test yourself 

```
python chi_square_pairs_test.py 
```

Use the `--help` flag to see the input parameters.

## Random and Pi Walk Tests on CF digits of Pi

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

## Random and Pi Sites visited Tests on CF digits of Pi

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



