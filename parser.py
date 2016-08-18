<<<<<<< HEAD
from html.parser import HTMLParser
from elastic_search import index


class Document:
=======
from HTMLParser import HTMLParser
from elastic_search import index

class Document():
>>>>>>> c407ef4bf4c02a80bd329877073bb5d88aced32b
    def __init__(self):
        self.id = ""
        self.title = ""
        self.h1 = []
        self.h2 = []
        self.h3 = []
        self.content = ""
<<<<<<< HEAD

    def setId(self, id):
        self.id = id

    def setTitle(self, title):
        self.title = title

    def addH1(self, h1):
        self.h1.append(h1)

    def addH2(self, h2):
        self.h2.append(h2)

    def addH3(self, h3):
        self.h3.append(h3)

=======
        
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
        
>>>>>>> c407ef4bf4c02a80bd329877073bb5d88aced32b
    def addContent(self, content):
        self.content += content + " "


# create a subclass and override the handler methods
class Parser(HTMLParser):
<<<<<<< HEAD
    def __init__(self):
        super().__init__()
        self.tag = ''
        self.doc = Document()

    def handle_starttag(self, tag, attrs):
        self.tag = tag

    def handle_endtag(self, tag):
        self.tag = ""

    def handle_data(self, data):
        if self.tag =='docno':
            self.doc.setId(data)
        elif self.tag == 'title':
            self.doc.setTitle(data)
        elif self.tag == "h1":
            self.doc.addH1(data)
        elif self.tag == "h2":
            self.doc.addH2(data)
        elif self.tag == "h3":
            self.doc.addH3(data)
        elif self.tag != "" and self.tag != "docoldno" and self.tag != "dochdr":
            self.doc.addContent(data)

    def start(self):
        index(self.doc)
=======
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
>>>>>>> c407ef4bf4c02a80bd329877073bb5d88aced32b
