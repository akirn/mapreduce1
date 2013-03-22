#!/usr/local/bin/python3

import sys

previous_key = None
total = 0

for line in sys.stdin:
    key, value = line.split("\t", 1)
    if key != previous_key:
        if previous_key != None:
            print(previous_key + " was found " + total + " times.")
        previous_key = key
        total = 0