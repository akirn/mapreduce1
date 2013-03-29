#!/usr/bin/env python

import sys
import re

counts = {}
regex = re.compile('[a-zA-Z]+')

for line in sys.stdin:
    words = line.split()
    for word in words:
        m = regex.match(word)
        if m is not None:
            print(m.group().lower() + "\t" + str(1))