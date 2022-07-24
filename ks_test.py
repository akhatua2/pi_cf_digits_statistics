import csv
from os import walk
import argparse
from scipy import stats
from tqdm import tqdm


def cmdline_args():
        # Make parser object
    p = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    
    p.add_argument("--filepath", type=str, default='results/100K-blocksize-10-groups/',
                   help="path to results")
    p.add_argument("--number_of_groups", type=int, default=10,
                help="the number of groups you wnat to split the numbers into")

    return(p.parse_args())

def ksTest(q_val: list):
    return stats.kstest(q_val, stats.chi2(args.number_of_groups).cdf)


if __name__ == '__main__':
    args = cmdline_args()
    filenames = next(walk(args.filepath), (None, None, []))[2] 

    p_val, q_val = [], []

    for file in tqdm(filenames):
        with open(args.filepath + file, mode ='r')as csv_reader:
            csvFile = csv.DictReader(csv_reader)

            for line in csvFile:
                p_val.append(float(line['p-value']))
                q_val.append(float(line['chi-square value']))
    print(len(q_val))
    print(ksTest(q_val))
        