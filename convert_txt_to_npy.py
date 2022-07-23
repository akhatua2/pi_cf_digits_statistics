from os import walk
import numpy as np
from tqdm import tqdm

def genBinFile(filename: str, outfile_name: str) -> None:
    with open(filename) as file:
        pi_dgits = [int(x) for x in file]
    np.save(outfile_name, pi_dgits)
    return


if __name__ == '__main__':
    mypath = 'raw_data/'
    filenames = next(walk(mypath), (None, None, []))[2] 
    for filename in tqdm(filenames):
        outfile_name = 'data/' + filename[:-4]
        genBinFile(mypath + filename, outfile_name)