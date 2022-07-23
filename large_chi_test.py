import numpy as np
from scipy import stats
import math
from collections import defaultdict
from tqdm import tqdm
import pandas as pd
from os import walk
from os.path import exists
import argparse
from utils import getLenDataText, getInputFiles

def cmdline_args():
        # Make parser object
    p = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    
    p.add_argument("--blocksize", type=int, default=1000000,
                   help="the size of each block")
    p.add_argument("--number_of_groups", type=int, default=10,
                   help="the number of groups you wnat to split the numbers into")

    p.add_argument("-v", "--verbosity", type=int, choices=[0,1], default=1,
                   help="increase output verbosity (default: %(default)s)")
    p.add_argument("--store", type=bool, default=False)

    return(p.parse_args())

def ChiSquare(data: list, blocksize: int, number_of_groups: int):
    p_val_arr = []
    q_res_arr = []
    number_of_blocks = len(data)/blocksize
    
    groups = list(np.array_split(data, number_of_blocks))
    
    def P(num_of_groups: int) -> list:
        res = []
        for k in range(1, num_of_groups+1):
            res.append(math.log(1+1/(k*(k+2)))/math.log(2))
        res.append(1-sum(res))
        return res

    def Y(number_of_groups: int, pi_digits: list) -> list:
        Y = [0] * (number_of_groups+1)
        for digit in pi_digits:
            if digit > number_of_groups:
                Y[-1] += 1
            else:
                Y[digit-1] += 1
        return Y

    def chisquare_test(y_array: list, blocksize: int, p_array: list, number_of_groups: int) -> list:
        q_val = 0
        for i in range(number_of_groups):
            q_val += ((y_array[i] - blocksize*p_array[i])**2)/(blocksize*p_array[i])
        return q_val
    
    for pi_cf_digits in groups:
        pi_digits = list(pi_cf_digits)
        
        y_array = Y(number_of_groups, pi_digits)
        assert(len(y_array) == (number_of_groups + 1))
        
        p_array = P(number_of_groups)
        assert(len(p_array) == (number_of_groups + 1))
        
        q_res = chisquare_test(y_array, blocksize, p_array, number_of_groups+1)
        
        p_val = 1 - stats.chi2.cdf(q_res , number_of_groups)
        p_val_arr.append(p_val)
        q_res_arr.append(q_res)
    assert(len(p_val_arr) == (number_of_blocks))
    assert(len(q_res_arr) == (number_of_blocks))
    return p_val_arr, q_res_arr


if __name__ == '__main__':
    args = cmdline_args()

    mypath = 'data/'
    filenames = next(walk(mypath), (None, None, []))[2] 
    left_over = []
    for file in tqdm(filenames):
        outname = file.split('.')[0][9:]
        filename = 'results/' + '1M-blocksize-10-groups/chi_results_' + outname  + '.csv'
        #print(filename)
        if exists(filename):
            #print('Exists. Going to the next one')
            continue
        pi_cf_digits = list(np.load(mypath + file)) + left_over
        num_digits = len(pi_cf_digits)
        mod = num_digits % args.blocksize
        if mod != 0:
            left_over = pi_cf_digits[num_digits - mod + 1:]
            pi_cf_digits = pi_cf_digits[:num_digits - mod]
        #print("Starting Chi-Square Test on " + getLenDataText(num_digits) + " continued fraction pi digits...")
        p_val_arr, q_res_arr = ChiSquare(pi_cf_digits, args.blocksize, args.number_of_groups)

        result = defaultdict(list)
        for p_val, q_val in zip(p_val_arr, q_res_arr):
            result['p-value'].append(p_val)
            result['chi-square value'].append(q_val)
        df = pd.DataFrame(data=result)
        #print("Printing results into " + filename)
        df.to_csv(filename) 