import json

from elasticsearch import Elasticsearch

articles = ["a", "the", "an"]
pronouns = ["i", "you", "we", "it", "they", "he", "she", "my", "mine", "their", "theirs", "his",
            "her", "that", "this", "us", "me", "him"]
connectives = ["in", "s", "d", "t", "by", "of", "out", "and", "or", "to", "as", "for", "on", "as", "so",
               "also", "though", "but", "not", "may", "who"]
verbs = ["is", "are", "been", "have", "do", "does"]

es = Elasticsearch(['http://localhost:9200'])
# es.indices.delete(index="docs")


def create_index():
    es.indices.create(index="docs")


def setup_index():
    f = open("parser.json", "w")
    f.write("")
    es.indices.close(index="foo")
    es.indices.put_settings(body={
        "settings": {
            "index": {
                "analysis": {
                    "analyzer": {
                        "analyzer_keyword": {
                            "tokenizer": "keyword",
                            "filter": "lowercase",
                            "stop_words": articles + connectives + verbs + pronouns
                        }
                    }
                }
            }
        },
        "mappings": {
            "t": {
                "properties": {
                    "title": {
                        "analyzer": "analyzer_keyword",
                        "type": "string"
                    },
                    "h1": {
                        "analyzer": "analyzer_keyword",
                        "type": "string"
                    },
                    "h2": {
                        "analyzer": "analyzer_keyword",
                        "type": "string"
                    },
                    "h3": {
                        "analyzer": "analyzer_keyword",
                        "type": "string"
                    },
                    "content": {
                        "analyzer": "analyzer_keyword",
                        "type": "string"
                    }
                }
            }
        }
    }, index="foo")
    es.indices.open(index="foo")


def index(doc):
    # json_doc = {
    #     "title": doc.title,
    #     "h1": doc.h1,
    #     "h2": doc.h2,
    #     "h3": doc.h3,
    #     "content": doc.content
    # }
    json_doc = json.dumps(doc.__dict__)
    f = open("parser.json", "a")
    f.write(json_doc + "\n")
    f.close()
    # res = es.index(index="docs", doc_type='webpage', id=doc.id, body=json_doc, ignore=[400])
    # print(res["_id"] + " indexed")


def search(query):
    res = es.search(q=query, filter_path=['hits.hits._id'])
    print(res)

# f = open("parser.json")
# for line in f.readline():
#     res = es.index(index="docs", doc_type='webpage', id=line.index, body=line, ignore=[400])
#     print(line.index , " indexed")
