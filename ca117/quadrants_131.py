#!/usr/bin/env python3

import sys

nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

for line in sys.stdin:
    x, y = [str(t) for t in line.strip().split()]
    if (x[0] in nums) and (y[0] in nums):
        print(1)
    elif (x[0] == '-') and (y[0] == '-'):
        print(3)
    elif (x[0] in nums) and (y[0] == '-'):
        print(2)
    else:
        print(4)
