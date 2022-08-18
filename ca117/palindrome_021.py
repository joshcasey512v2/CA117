#!/usr/bin/env python3

import sys
from string import punctuation


lines = sys.stdin.readlines()

for line in lines:
    s = line.lower().strip()
    for c in s:
        if c in punctuation or c == " ":
            s = s.replace(c, "", 1)
    print(s == s[::-1])
