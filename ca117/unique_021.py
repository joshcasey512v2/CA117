#!/usr/bin/env python3

import sys

from string import punctuation

seen = []

words = sys.stdin.read().lower().split()
#    print(len(words))

for word in words:
    for c in word:
       if c in punctuation:
           word = word.replace(c, "")
    if word not in seen and word != '':
       seen.append(word)

#print(sorted(seen))
print(len(seen))
