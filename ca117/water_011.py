#!/usr/bin/env python3

import sys

n = int(input())

a = []

s = input()
b = s.split(" ")


tot = 0
i = 0
while i < len(b):
    t = int(b[i])
    tot = tot + t
    if tot <= n:
        a.append(tot)
    i = i + 1

print(len(a))
