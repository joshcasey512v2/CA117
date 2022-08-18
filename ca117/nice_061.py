#!/usr/bin/env python3

import sys

nice = set('nice')

for line in sys.stdin:
    words = line.strip()
    for c in words:
         if words.count(c) > 1:
             words = words.replace(words, "")
     if set(words).issuperset(nice):
         print("".join(words))
