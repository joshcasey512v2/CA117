#!/usr/bin/env python3

import sys

lang = []
trans = {}


with open(sys.argv[1], 'r') as f:
    for line in f:
        words = line.strip().split()
        lang.append(words[1])

for i in range(11):
    trans[i] = lang[i]

for nums in sys.stdin:
    nums = nums.strip().split()
    a = []
    for j in range(len(nums)):
        a.append(int(nums[j]))
    b = []
    for t in range(len(a)):
        b.append(trans[a[t]])
    print(" ".join(b))
