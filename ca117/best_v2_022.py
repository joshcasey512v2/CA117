#!/usr/bin/env python3

import sys

try:

    with open(sys.argv[1], 'r') as f:
        mxlen = 0
        for line in f:
            s = line.strip().split()
            if int(s[0]) > mxlen:
                mxlen = int(s[0])
           

except ValueError:
    print("Invalid mark", s[0], "encountered. Exiting.")
