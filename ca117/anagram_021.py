#!/usr/bin/env python3

import sys

a = []

for line in sys.stdin:
    [left, right] = line.strip().split()
    if len(left) == len(right):
        for c in left:
            if c in right:
                right = right.replace(c, "", 1)
        print(not right)
    else:
        print("False")
