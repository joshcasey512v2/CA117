#!/usr/bin/env python3

import sys


for line in sys.stdin:
    s = line.strip()
    n = int(s)
    a = []
    for num in range(1, n + 1):
        if num % 3 == 0:
            a.append("X")
        else:
            a.append(num)
    print("Multiples of 3 replaced:", a)
