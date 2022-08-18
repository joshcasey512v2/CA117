#!/usr/bin/env python3

import sys

vowels = ['aa', 'ee', 'ii', 'oo', 'uu']

double = []

for line in sys.stdin:
    line = line.strip()
    for i in vowels:
        if i in line:
            double.append(line)

print(double)
#print(max(double, key=len))
