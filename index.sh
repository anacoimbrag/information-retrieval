#!/bin/bash

index=foo

echo 'Creating index ...'
curl -XPOST "http://localhost:9200/$index/"
echo -ne "\nIndex $index created\n"

echo "----------------------------------------------------------"

# create json file with docs
echo "Reading files ..."
python3 run.py &
pid=$! # Process Id of the previous running command

spin='-\|/'

i=0
while kill -0 ${pid} 2>/dev/null
do
  i=$(( (i+1) %4 ))
  printf "\r${spin:$i:1}"
  sleep .1
done
echo "Extracted data on parser.json"

echo "----------------------------------------------------------"

echo "Indexing documents ..."
cat parser.json | ./stream2es &
pid=$! # Process Id of the previous running command

spin='-\|/'

i=0
while kill -0 ${pid} 2>/dev/null
do
  i=$(( (i+1) %4 ))
  printf "\r${spin:$i:1}"
  sleep .1
done
echo "Documents indexed"

echo "----------------------------------------------------------"

echo "Index stats: "
curl "http://localhost:9200/$index/_stats/indexing,search?pretty"