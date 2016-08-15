import operator

text = ""
number_of_relevance_words = 10


def clean_text(txt):
    special = '\'"`,.(){}[];,<>-_|:$%@!&*?/#\\'
    for char in special:
        txt = str(txt).replace(char, " ")
    return txt.lower()


# def extract_info(txt):
#     global text
#     text = txt
#     print(text)
#     print("Id: " + get_doc_id())
#     print("Title: " + get_title())
#     for h1 in get_h1():
#         print("H1: " + h1)
#     for h2 in get_h2():
#         print("H2: " + h2)
#     for h3 in get_h3():
#         print("H3: " + h3)
#     print(get_relevant_words())


def get_doc_id():
    return text[:text.find(" ")]


def get_title():
    for line in text.split("\n"):
        if str(line).startswith("#t"):
            title = str(line)[str(line).find("#t") + 2:].strip()
            return title
    return ""


def get_h1():
    h1 = []
    for line in text.split("\n"):
        if str(line).startswith("# "):
            h1.append(str(line)[str(line).find("#") + 1:].strip())
    return h1


def get_h2():
    h2 = []
    for line in text.split("\n"):
        if str(line).startswith("## "):
            h2.append(str(line)[str(line).find("##") + 2:].strip())
    return h2


def get_h3():
    h3 = []
    for line in text.split("\n"):
        if str(line).startswith("### "):
            h3.append(str(line)[str(line).find("###") + 3:].strip())
    return h3


def get_words():
    index = text.find("body")
    txt = text[index:]
    txt = clean_text(txt)
    return txt.split()


def takeoff_useless_words():
    articles = ["a", "the", "an"]
    pronouns = ["i", "you", "we", "it", "they", "he", "she", "my", "mine", "their", "theirs", "his",
                "her", "that", "this", "us", "me", "him"]
    connectives = ["in", "s", "d", "t", "by", "of", "out", "and", "or", "to", "as", "for", "on", "as", "so",
                   "also", "though", "but", "not", "may", "who"]
    verbs = ["is", "are", "been", "have", "do", "does"]
    words = get_words()
    words = [word for word in words if word not in articles and word not in pronouns and
             word not in connectives and word not in verbs]

    # for word in words:
        # print(word)

    return words


def get_relevant_words():
    words = takeoff_useless_words()
    counted_words = dict()
    for word in words:
        if word not in counted_words:
            counted_words[word] = 1
        else:
            counted_words[word] += 1

    sorted_words = sorted(counted_words.items(), key=operator.itemgetter(1), reverse=True)
    # print(sorted_words)
    return list(dict(sorted_words).keys())


class Document:
    def __init__(self, txt):
        global text
        text = txt

        self.id = get_doc_id()
        self.title = get_title()
        self.h1 = get_h1()
        self.h2 = get_h2()
        self.h3 = get_h3()
        self.relevant_words = get_relevant_words()
