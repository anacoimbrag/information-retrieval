import gzip
import os

from elastic_search import search, index
from parser import Parser


def separate_docs(content):
    return content.split("<doc>")


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
