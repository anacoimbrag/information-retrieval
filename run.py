import datetime

from elastic_search import setup_index
from read_files import read_files

f = open("parser.json", "w")
f.write("")

setup_index()
start = datetime.datetime.now()

read_files()

finish = datetime.datetime.now()
print("Finished - " + str(finish - start))

