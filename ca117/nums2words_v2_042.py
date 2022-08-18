#!/usr/bin/env python3

import sys

eng = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three',
       '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
       '8': 'eight', '9': 'nine', '10': 'ten'}

for lines in sys.stdin:
    nums = lines.strip().split()
    a = []
    for i in range(len(nums)):
        if nums[i] in eng:
            a.append(eng[nums[i]])
        else:
            a.append("unknown")
    print(" ".join(a))
