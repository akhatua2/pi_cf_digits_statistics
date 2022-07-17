import numpy as np
from scipy import stats
import math
from collections import defaultdict
from tqdm import tqdm
import pandas as pd
import argparse
from utils import getLenDataText, getInputFiles

def cmdline_args():
        # Make parser object
    p = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    
    p.add_argument("--pi_cf_digits_filename", default='data/iteration1_int.npz',
                   help="desc")
    p.add_argument("--number_of_pi_cf_digits", type=int, default=1000000000,
                   help="desc")
    p.add_argument("--blocksize", type=int, default=100000,
                   help="req number")
    p.add_argument("--number_of_pairs", type=int, default=5,
                   help="include to enable")

    p.add_argument("-v", "--verbosity", type=int, choices=[0,1], default=1,
                   help="increase output verbosity (default: %(default)s)")

    return(p.parse_args())

def ChiSquarePairs(data: list, blocksize: int, pairs: int=5):
    p_val_arr = []
    q_res_arr = []
    number_of_blocks = len(data)/blocksize
    
    groups = list(np.array_split(data, number_of_blocks))
    
    def P(pairs: int) -> list:
        p_dict = {}
        for a in (range(1, pairs+1)):
            for b in range(1, pairs+1):
                prob = math.log(((a*b + a + b + 2)*(a*b + 1))/((a*b + a + 1)*(a*b + b + 1)))/math.log(2)
                p_dict[(a, b)] = prob
        p_dict['else'] = 1 - sum(list(p_dict.values()))
        return p_dict

    def Y(pi_digits: list, pairs: int) -> list:
        y_dict = defaultdict(int)
        for a, b in zip(pi_digits[:-1], pi_digits[1:]):
            if a <=pairs and b <= pairs:
                y_dict[(a, b)] += 1
            else:
                y_dict['else'] += 1
        return y_dict
    
    def chisquare_test(y_array: list, p_array: list, blocksize: int, pairs: int) -> list:
        q_val = 0
        for a in (range(1, pairs+1)):
            for b in range(1, pairs+1):
                q_val += ((y_array[(a, b)] - blocksize*p_array[(a, b)])**2)/(blocksize*p_array[(a, b)])
        return q_val
    p_array = P(pairs)
    for pi_cf_digits in tqdm(groups, disable=not(args.verbosity)):
        pi_digits = list(pi_cf_digits)

        y_array = Y(pi_digits, pairs)
        
        q_res = chisquare_test(y_array, p_array, blocksize, pairs)
        p_val = 1 - stats.chi2.cdf(q_res , len(p_array))
        
        p_val_arr.append(p_val)
        q_res_arr.append(q_res)

    result = defaultdict(list)
    for p_val, q_val in zip(p_val_arr, q_res_arr):
        result['p-value'].append(p_val)
        result['chi-square value'].append(q_val)
    df = pd.DataFrame(data=result)
    filename = 'chisq-pairs-' + getLenDataText(len(data)) +'-digits-' + \
                getLenDataText(int(number_of_blocks)) + '-blocks'
    print("\nPrinting results into " + filename)
    df.to_csv('results/' + filename + '.csv') 
    return p_val_arr, q_res_arr

if __name__ == '__main__':
    args = cmdline_args()
    print(args)
    pi_cf_digits = getInputFiles(args)
    print("\nStarting Chi-Square Test for " + getLenDataText(args.number_of_pi_cf_digits) + \
        " continued fraction pi digits...")
    p_val_arr, q_res_arr = ChiSquarePairs(pi_cf_digits, args.blocksize, args.number_of_pairs)
    print("The KS-test results are: ", stats.kstest(q_res_arr, stats.chi2(args.number_of_pairs**2 + 1).cdf))
    
    
