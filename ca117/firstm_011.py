#!/usr/bin/env python3

import sys

def replace(s):
    return s.replace('m', 'M', 1)


for line in sys.stdin:
    s = line.strip()
    t = replace(s)
    print(t)
