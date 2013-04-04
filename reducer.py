#!/usr/bin/env python

import sys

def output(key, total):
    if key is not None:
            print(str(total) + "\t" + key)

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