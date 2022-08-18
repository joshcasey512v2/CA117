#!/usr/bin/env python3

import sys

def chop(s):
	return s[1:len(s) - 1]

for line in sys.stdin:
	s = line.strip()
	chopped = chop(s)
	print(chopped)
