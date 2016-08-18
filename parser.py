from HTMLParser import HTMLParser
from elastic_search import index

class Document():
    def __init__(self):
        self.id = ""
        self.title = ""
        self.h1 = []
        self.h2 = []
        self.h3 = []
        self.content = ""
        
    def setId(self, id):
        self.id = id
    
    def setTitle(self, title):
        self.title = title
        
    def addH1(self, h1):
        self.append(h1)
        
    def addH2(self, h2):
        self.append(h2)
        
    def addH3(self, h3):
        self.append(h3)
        
    def addContent(self, content):
        self.content += content + " "


# create a subclass and override the handler methods
class Parser(HTMLParser):
    tag = ""
    doc = Document()
    
    def handle_starttag(self, tag, attrs):
        tag = tag

    def handle_endtag(self, tag):
        tag = ""

    def handle_data(self, data):
        if tag == "DOCNO":
            doc.setId(data)
        if tag == "title":
            doc.setTitle(data)
        if tag == "h1":
            doc.addH1(data)
        if tag == "h2":
            doc.addH2(data)
        if tag == "h3":
            doc.addH4(data)
        elif tag != "":
            doc.addContent(data)

    def start():
        index(doc)
