#!/usr/bin/env python3

import sys

def sub(s):
    return s.upper()


for line in sys.stdin:
    s = line.strip()
    subs = sub(s).split()
    if subs[0] in subs[1]:
        print("True")
    else:
        print("False")
