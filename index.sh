#!/bin/bash

# create json file with docs
python3 run.py

# index - stream to es
cat parser.json | ./stream2es