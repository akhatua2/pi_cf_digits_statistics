from tqdm import tqdm
import numpy as np
from os import walk

BILLION = 1000000000
MILLION = 1000000
THOUSAND = 1000
FILE_SIZE = 350000000

def getLenDataText(len_data: int) -> str:   
    if len_data/BILLION >= 1:
        suffix='B'
        prefix = str(int(len_data/BILLION))
    elif len_data/MILLION >= 1:
        suffix='M'
        prefix = str(int(len_data/MILLION))
    elif len_data/THOUSAND >= 1:
        suffix='K'
        prefix = str(int(len_data/THOUSAND))
    else:
        suffix = ''
        prefix = str(int(len_data))
    return prefix+suffix
    
def getInputFiles(args) -> list:
    print("Loading ", getLenDataText(args.number_of_pi_cf_digits) + \
        ' continued fraction digits of pi...')
    mypath = 'data/'
    filenames = next(walk(mypath), (None, None, []))[2] 
    num_files = (args.number_of_pi_cf_digits//FILE_SIZE) + 1
    pi_cf_digits = []
    for i in tqdm(range(num_files), disable=not(args.verbosity)):
        pi_digits = np.load(mypath + filenames[i])
        pi_cf_digits.extend(pi_digits['arr_0'])
    pi_cf_digits = pi_cf_digits[1:(args.number_of_pi_cf_digits+1)]
    #pi_cf_digits = pi_cf_digits[:math.floor((len(pi_cf_digits)/args.blocksize))* args.blocksize]
    return pi_cf_digits