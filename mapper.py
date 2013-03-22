#!/usr/local/bin/python3

import sys

counts = {}

for line in sys.stdin:
    words = line.split()
    for word in words:
        print(word + "\t" + str(1))