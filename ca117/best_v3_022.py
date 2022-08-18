#!/usr/bin/env python3

import sys


a = []

with open(sys.argv[1], 'r') as f:
    mxlen = 0
    for line in f:
        try:
            a.append(line.strip())
            d = line.strip().split()
            if int(d[0]) > mxlen:
                mxlen = int(d[0])
        except ValueError:
            print("Invalid mark", d[0], "encountered. Skipping.")

for i in range(len(a)):
    if str(mxlen)in a[i]:
        student = a[i][3:]
        break

print("Best student:", student)
print("Best mark:", mxlen)
