#!/usr/bin/env python

import sys
import re

counts = {}

for line in sys.stdin:
    words = re.findall(r"\w+", line)
    for word in words:
        print(word.lower() + "\t" + str(1))