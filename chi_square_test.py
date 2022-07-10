import numpy as np
from scipy import stats
import math
from collections import defaultdict
from tqdm import tqdm
import pandas as pd
import os 
import argparse

def cmdline_args():
        # Make parser object
    p = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    
    p.add_argument("--pi_cf_digits_filename", default='iteration1_int.npz',
                   help="desc")
    p.add_argument("--number_of_pi_cf_digits", type=int, default=10000000,
                   help="desc")
    p.add_argument("--blocksize", type=int, default=1000000,
                   help="req number")
    p.add_argument("--number_of_groups", type=int, default=5,
                   help="include to enable")

    p.add_argument("-v", "--verbosity", type=int, choices=[0,1], default=1,
                   help="increase output verbosity (default: %(default)s)")

    return(p.parse_args())

def ChiSquare(data, blocksize=100, number_of_groups=5, verbosity=0):
    p_val_arr = []
    q_res_arr = []
    number_of_blocks = len(data)/blocksize
    
    groups = list(np.array_split(data, number_of_blocks))
    
    def P(num_of_groups):
        res = []
        for k in range(1, num_of_groups+1):
            res.append(math.log(1+1/(k*(k+2)))/math.log(2))
        res.append(1-sum(res))
        return res

    def Y(number_of_groups, pi_digits):
        Y = [0] * (number_of_groups+1)
        for digit in pi_digits:
            if digit > number_of_groups:
                Y[-1] += 1
            else:
                Y[digit-1] += 1
        return Y

    def chisquare_test(y_array, blocksize, p_array, number_of_groups):
        q_val = 0
        for i in range(number_of_groups):
            q_val += ((y_array[i] - blocksize*p_array[i])**2)/(blocksize*p_array[i])
        return q_val
    
    for pi_cf_digits in tqdm(groups, disable=verbosity):
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
    
    result = defaultdict(list)
    for p_val, q_val in zip(p_val_arr, q_res_arr):
        result['p-value'].append(p_val)
        result['chi-square value'].append(q_val)
    df = pd.DataFrame(data=result)
    filename = 'chi-square-results-' + str(len(data)) +'-digits-' + \
                str(int(number_of_blocks)) + '-blocks-' + str(number_of_groups) \
                + '-groups'
    df.to_csv(filename + '.csv') 
    return p_val_arr, q_res_arr


if __name__ == '__main__':
    args = cmdline_args()
    pi_digits = np.load(args.pi_cf_digits_filename)
    pi_cf_digits = list(pi_digits['arr_0'])[1:(args.number_of_pi_cf_digits+1)]
    p_val_arr, q_res_arr = ChiSquare(pi_cf_digits, args.blocksize, args.number_of_groups, 1 - args.verbosity)
    
    
