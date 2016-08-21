# Information Retrieval

## Requirements

To run this project you need to have installed:
* [Python 3.5](https://www.python.org/)
* [Python pip](https://pypi.python.org/pypi/pip)
* [Java 7+](http://www.oracle.com/technetwork/java/javase/downloads/index.html) - Just for Elasticsearch to run
* [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html#jvm-version)

### Installing Elasticsearch

To install this search engine, download it from the [official site](https://www.elastic.co/downloads/elasticsearch)
and unzip it to this project root folder.

### Installing Python dependencies

After installing pip, run on terminal
```bash
$ pip install -r requirements.txt
```
remember that you need to be `root` or run as `sudo`

## Running

Before running this program, we have to start elasticsearch. If the elasticsearch folder is in the project root folder,
you can do that just doing
```bash
$ ./start.sh
```

if not, go to elasticsearch root folder and run `./elasticsearch` from `elasticsearch-version/bin`

After elasticsearch is running, open another terminal window and type `./index.sh` to run the project
This will read all files from WT10G/sample folder and index them to __foo__ index in elasticsearch running on your machine