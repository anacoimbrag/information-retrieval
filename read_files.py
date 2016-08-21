import gzip
import os

from parser import Parser

path = os.getcwd() + "/WT10G/sample"


def separate_docs(content):
    return content.split("<doc>")


def read_files():

    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".gz"):
                print("----Arquivo %r ----" % name)
                file = gzip.open(os.path.join(root, name), 'rb')
                text = str(file.read())
                text = text.replace("\\r", "").replace("\\n", " ").replace("\\'", "'").replace("\\b", "").lower()
                docs = separate_docs(text)
                for doc in docs:
                    if doc != "b'":
                        parser = Parser()
                        parser.feed(doc)
                        parser.start()
