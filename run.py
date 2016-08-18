import multiprocessing as mp
import os

import datetime

from elastic_search import setup_index, create_index
from read_files import read_files

path = os.getcwd() + "/WT10G/sample/"

pool = mp.Pool(mp.cpu_count())
setup_index()
start = datetime.datetime.now()
namefiles = []
for root, dir, files in os.walk(path):
    for name in files:
        namefiles.append(os.path.join(root, name))

print("Started")
pool.map_async(read_files, namefiles)
pool.close()
pool.join()
finish = datetime.datetime.now()
print("Finished " + str(finish - start))
