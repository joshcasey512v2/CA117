#!/usr/bin/env python3

import sys
from string import punctuation

used = []

for line in sys.stdin:
    line = line.strip().split()
    output = []
    for word in line:
        if word.lower().strip(punctuation) not in used:
            used.append(word.lower().strip(punctuation))
            output.append(word)
        else:
            output.append('.')
    print(" ".join(output))
