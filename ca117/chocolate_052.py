#!/usr/bin/env python3

import sys

for line in sys.stdin:
    words = line.strip()
    nums = int(words)
    print((nums + 300) // 400)
