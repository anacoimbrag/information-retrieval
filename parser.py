from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class Parser(HTMLParser):
    tag = ""
    doc = new Document()
    
    def handle_starttag(self, tag, attrs):
        tag = tag
        print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        tag = ""
        print "Encountered an end tag :", tag

    def handle_data(self, data):
        print "Encountered some data  :", data
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
        
class Document():
    def __init__():
        id = ""
        title = ""
        h1 = []
        h2 = []
        h3 = []
        content = ""
        
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
