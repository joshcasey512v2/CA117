#!/usr/bin/env python3

import sys

for line in sys.stdin:
    s = line.strip()
    i = 0
    while i < len(s) and s[i] != ".":
        i = i + 1
    j = i
    while j < len(s) and not (s[j] >= "0" and s[j] <= "9"):
        j = j + 1

    print(s[0].upper() + s[1:i], s[i + 1].upper() + s[i + 2:j])
