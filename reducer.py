#!/usr/local/bin/python3

import sys

def output(key, total):
    if key != None:
            print(key + " was found " + total + " times.")

previous_key = None
total = 0

for line in sys.stdin:
    key, value = line.split("\t", 1)
    if key != previous_key:
        output(previous_key, total)
        previous_key = key
        total = 0

    total += int(value)

output(previous_key, total)