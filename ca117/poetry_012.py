#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()


mxlen = -1
for line in lines:
    if len(line.strip()) > mxlen:
        mxlen = len(line.strip())

for line in lines:
    print(f'{line.strip():^{mxlen:d}s}')
