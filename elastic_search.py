from elasticsearch import Elasticsearch

from extract_info import Document

es = Elasticsearch(['http://localhost:9200'])


def index(doc):
    idx = doc.id[doc.id.find("-") + 1:doc.id.find("-", doc.id.find("-") + 1)].lower()
    print(doc.title)
    res = es.index(index=idx, doc_type='webpage', id=doc.id, body=json_doc, ignore=[400])
    print(res["_id"] + " indexed")


def search(query):
    res = es.search(q=query, filter_path=['hits.hits._id'])
    print(res)

