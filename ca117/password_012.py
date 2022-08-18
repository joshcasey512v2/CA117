#!/usr/bin/env python3

import sys


for line in sys.stdin:
    s = line.strip()
    a = [0, 0, 0, 0]
    for c in s:
        if c.isdigit():
            a[0] = 1
        elif c.islower():
            a[1] = 1
        elif c.isupper():
            a[2] = 1
        else:
            a[3] = 1
    print(sum(a))
