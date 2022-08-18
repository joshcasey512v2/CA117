#!/usr/bin/env python3

import sys

from math import pi

for line in sys.stdin:
    s = line.strip()
    n = int(s)
    print(f'{pi:.{n}f}')
