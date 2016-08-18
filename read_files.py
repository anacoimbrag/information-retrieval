import gzip
import os

<<<<<<< HEAD
from elastic_search import search, index
from parser import Parser
=======
from elastic_search import index, search
import parser

path = os.getcwd() + "/WT10G/sample"
>>>>>>> c407ef4bf4c02a80bd329877073bb5d88aced32b


def separate_docs(content):
    return content.split("<doc>")

<<<<<<< HEAD
=======
for root, dirs, files in os.walk(path):
    for name in files:
        if not name.startswith("."):
            print("----Arquivo %r ----" % name)
            file = gzip.open(os.path.join(root, name), 'rb')
            text = str(file.read())
            text = text.replace("\\r", "").replace("\\n", " ").replace("\\'", "'").replace("\\b", "").lower()
            docs = separate_docs(text)
            for doc in docs:
                if doc != "b'":
                    p = Parser()
                    p.feed(doc)
                    p.start(t)
>>>>>>> c407ef4bf4c02a80bd329877073bb5d88aced32b

def read_files(filename):

    # for root, dirs, files in os.walk(path):
        # for name in files:
    if filename.endswith(".gz"):
        print("----Arquivo %r ----" % filename)
        file = gzip.open(filename, 'rb')
        text = str(file.read())
        text = text.replace("\\r", "").replace("\\n", " ").replace("\\'", "'").replace("\\b", "").lower()
        docs = separate_docs(text)
        for doc in docs:
            if doc != "b'":
                parser = Parser()
                parser.feed(doc)
                parser.start()

# search("do beavers live in salt water")
