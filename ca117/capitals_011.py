#!/usr/bin/env python3

import sys

def cap(s):
    return s[0].upper() + s[1:len(s) - 1] + s[-1].upper()


for line in sys.stdin:
    s = line.strip()
    capital = cap(s)
    if len(s) > 1:
        print(capital)
