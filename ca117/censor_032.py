#!/usr/bin/env python3

import sys

cen = []

with open(sys.argv[1], 'r') as f:
	for words in f:
		words = words.strip()
		cen.append(words)

for lines in sys.stdin:
	text = lines.strip().split()
	for i in cen:
		if i in text:
			text = text.replace(text, "@", 1)
	print(text)

print(cen)