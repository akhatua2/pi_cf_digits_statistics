import numpy as np
from scipy import stats
from tqdm import tqdm
import argparse
from utils import getRandDistribution, getInputFiles, getMoves, getSingleRandomWalk, getSinglePiWalk
import random


def cmdline_args():
        # Make parser object
    p = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    
    p.add_argument("--number_of_pi_cf_digits", type=int, default=1000,
                   help="the number of CF digits of pi in each run")
    p.add_argument("--num_runs", type=int, default=10,
                   help="the size of each block")

    p.add_argument("-v", "--verbosity", type=int, choices=[0,1], default=1,
                   help="increase output verbosity (default: %(default)s)")
    p.add_argument("--use_rand", type=bool, default=False)
    p.add_argument("--mod", type=int, default=6)

    return(p.parse_args())

def randWalk(mod: int) -> list:
    distribution = getRandDistribution(args, mod)
    inv_distribution = [1/distribution[i] for i in range(len(distribution))]
    moves = getMoves(inv_distribution, mod)
    avg_distances = []
    for _ in tqdm(range(args.num_runs)):
        rand_distribution = random.choices([i for i in range(mod)], weights = distribution, k = args.number_of_pi_cf_digits)
        avg_distances.append(getSingleRandomWalk(rand_distribution, moves, args, mod))
    return avg_distances

def piWalk(pi_cf_digits: list, mod: int) -> list:
    distribution = getRandDistribution(args, mod)
    inv_distribution = [1/distribution[i] for i in range(len(distribution))]
    moves = getMoves(inv_distribution, mod)
    groups = list(np.array_split(pi_cf_digits, args.num_runs))
    avg_distances = []
    for i in tqdm(range(args.num_runs)):
        avg_distances.append(getSinglePiWalk(groups[i], moves, args, mod))
    return avg_distances

if __name__ == '__main__':
    args = cmdline_args()
    print('\033[1;32m' + str(args) + '\n')
    if args.use_rand:
        result = randWalk(args.mod)
    else:
        pi_cf_digits = getInputFiles(args, True)
        random.shuffle(pi_cf_digits)
        result = piWalk(pi_cf_digits, args.mod)
    print(stats.describe(result))