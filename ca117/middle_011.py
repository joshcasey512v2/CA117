#!/usr/bin/env python3

import sys

def mid(s):
    return s[len(s) // 2]


for line in sys.stdin:
    s = line.strip()
    middle = mid(s)
    if len(s) % 2 != 0:
        print(middle)
    else:
        print("No middle character!")
