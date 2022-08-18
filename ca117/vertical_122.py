#!/usr/bin/env python3

import sys

def lower_w(n):
   return n.lower()


words = [line.strip() for line in sys.stdin]

horizontal = []

for i in range(len(words[0])):
   new_w = ''
   for line in words:
      new_w = new_w + line[i]
   horizontal.append(new_w)

sorted_horizontal = sorted(horizontal, key=lower_w)
correct = []

for i in range(len(sorted_horizontal[0])):
   new_wo = ''
   for line in sorted_horizontal:
      new_wo = new_wo + line[i]
   correct.append(new_wo)

for i in correct:
   print(i)
