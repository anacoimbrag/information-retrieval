from html.parser import HTMLParser
from elastic_search import index


class Document:
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
        self.h1.append(h1)

    def addH2(self, h2):
        self.h2.append(h2)

    def addH3(self, h3):
        self.h3.append(h3)

    def addContent(self, content):
        self.content += content + " "


# create a subclass and override the handler methods
class Parser(HTMLParser):
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
