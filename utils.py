from tqdm import tqdm
import numpy as np
from os import walk
import math
import random

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
    
def getInputFiles(args, walks: bool=False) -> list:
    total_pi_cf_digits = args.number_of_pi_cf_digits
    if walks:
        total_pi_cf_digits = args.number_of_pi_cf_digits*args.num_runs

    print("Loading ", getLenDataText(total_pi_cf_digits) + \
        ' continued fraction digits of pi...')
    mypath = 'data/'
    filenames = next(walk(mypath), (None, None, []))[2] 
    num_files = (total_pi_cf_digits//FILE_SIZE) + 1
    pi_cf_digits = []
    for i in tqdm(range(num_files), disable=not(args.verbosity)):
        pi_digits = np.load(mypath + filenames[i])
        pi_cf_digits.extend(pi_digits['arr_0'])
    pi_cf_digits = pi_cf_digits[1:(total_pi_cf_digits+1)]
    return pi_cf_digits

def getRandDistribution(args, mod: int=4) -> list:
    nums = [math.log(1+1/(k*(k+2)))/math.log(2) for k in range(1, args.number_of_pi_cf_digits+1)]
    distribution = [0 for i in range(mod)]
    for i in range(len(nums)):
        distribution[i%mod] += nums[i]
    return distribution

def getMoves(weights: list, mod: int=4) -> list:
    if mod == 4:
        moves = [(1*weights[0], 0),
                (0, 1*weights[1]),
                (-1*weights[2], 0),
                (0, -1*weights[3])]
    elif mod == 6:
        moves = [(1*weights[0], 0, 0),
                (0, 1*weights[1], 0),
                (-1*weights[2], 0, 0),
                (0, -1*weights[3], 0),
                (0, 0, 1*weights[4]),
                (0, 0, -1*weights[5])]
    else:
        moves = []
    return moves

def getDistFromOrigin(coordinates, mod: int=4) -> float:
    if mod == 4:
        return float(math.sqrt((coordinates[0]**2) \
                       + (coordinates[1]**2)))
    elif mod == 6:
        return float(math.sqrt((coordinates[0]**2) \
                       + (coordinates[1]**2) \
                       + (coordinates[2]**2)))
    else:
        return -1.0

def getSingleRandomWalk(random_dist, moves, args, mod: int=4) -> float:
    if mod == 4:
        random_walk = [(0, 0)]
        for digit in random_dist:
            random_walk.append((random_walk[-1][0] + moves[digit][0], \
                                random_walk[-1][1] + moves[digit][1]))
        distance = 0
        for coord in random_walk[1:]:
            distance += getDistFromOrigin(coord)
        avg_dist = float(distance/args.number_of_pi_cf_digits * 500*math.pi)
    elif mod == 6:
        random_walk = [(0, 0, 0)]
        for digit in random_dist:
            random_walk.append((random_walk[-1][0] + moves[digit][0], \
                                random_walk[-1][1] + moves[digit][1], \
                                random_walk[-1][2] + moves[digit][2]))
        distance = 0
        for coord in random_walk[1:]:
            distance += getDistFromOrigin(coord, mod)
        avg_dist = float(distance/args.number_of_pi_cf_digits * 500*math.pi)
    else:
        avg_dist = -1.0
    return avg_dist

def getSingleRandomSitesVisited(random_dist, moves, mod: int=4) -> int:
    if mod == 4:
        random_walk = [(0, 0)]
        for digit in random_dist:
            random_walk.append((random_walk[-1][0] + moves[digit][0], \
                                random_walk[-1][1] + moves[digit][1]))
        sites = set()
        for coord in random_walk:
            sites.add((math.floor(coord[0]), math.floor(coord[1])))
    elif mod == 6:
        random_walk = [(0, 0, 0)]
        for digit in random_dist:
            random_walk.append((random_walk[-1][0] + moves[digit][0], \
                                random_walk[-1][1] + moves[digit][1], \
                                random_walk[-1][2] + moves[digit][2]))
        sites = set()
        for coord in random_walk:
            sites.add((math.floor(coord[0]), math.floor(coord[1]), math.floor(coord[2])))
    else:
        sites = set()
    return len(sites)

def getSinglePiWalk(pi_cf_digits, moves, args, mod: int=4) -> float:
    if mod == 4:
        pi_dist = [(digit-1)%mod for digit in pi_cf_digits]
        pi_walk = [(0, 0)]
        for digit in pi_dist:
            pi_walk.append((pi_walk[-1][0] + moves[digit][0], pi_walk[-1][1] + moves[digit][1]))
        distance = 0
        for coord in pi_walk[1:]:
            distance += getDistFromOrigin(coord)
        avg_dist = float(distance/(args.number_of_pi_cf_digits * 500*math.pi))
    elif mod == 6:
        pi_dist = [(digit-1)%mod for digit in pi_cf_digits]
        pi_walk = [(0, 0, 0)]
        for digit in pi_dist:
            pi_walk.append((pi_walk[-1][0] + moves[digit][0], \
                            pi_walk[-1][1] + moves[digit][1], \
                            pi_walk[-1][2] + moves[digit][2]))
        distance = 0
        for coord in pi_walk[1:]:
            distance += getDistFromOrigin(coord, mod)
        avg_dist = float(distance/(args.number_of_pi_cf_digits * 500*math.pi))
    else:
        avg_dist = -1.0
    return avg_dist

def getSinglePiSitesVisited(pi_cf_digits, moves, mod: int=4) -> int:
    if mod == 4:
        pi_dist = [(digit-1)%mod for digit in pi_cf_digits]
        pi_walk = [(0, 0)]
        for digit in pi_dist:
            pi_walk.append((pi_walk[-1][0] + moves[digit][0], pi_walk[-1][1] + moves[digit][1]))
        sites = set()
        for coord in pi_walk:
            sites.add((math.floor(coord[0]), math.floor(coord[1])))
    elif mod == 6:
        pi_dist = [(digit-1)%mod for digit in pi_cf_digits]
        pi_walk = [(0, 0, 0)]
        for digit in pi_dist:
            pi_walk.append((pi_walk[-1][0] + moves[digit][0], \
                            pi_walk[-1][1] + moves[digit][1], \
                            pi_walk[-1][2] + moves[digit][2]))
        sites = set()
        for coord in pi_walk:
            sites.add((math.floor(coord[0]), math.floor(coord[1]), math.floor(coord[2])))
    else:
        sites = set()
    return len(sites)