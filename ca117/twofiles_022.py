#!/usr/bin/env python3

import sys

a = []
b = []

with open(sys.argv[1], 'r') as f:
    for line in f:
        s = line.strip()
        a.append(int(s))

with open(sys.argv[2], 'r') as q:
    for line in q:
        n = line.strip()
        b.append(int(n))


#x = (list(zip(a, b)))


i = 0
while i < len(a):
    print(a[i])
    print(b[i])
    i = i + 1
