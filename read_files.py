import gzip
import os

from elastic_search import index, search
import html2txt

path = os.getcwd() + "/WT10G/sample"


def separate_docs(content):
    return content.split("<doc>")

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
                    t = html2txt.html2text(doc)
                    index(t)


search("do beavers live in salt water")