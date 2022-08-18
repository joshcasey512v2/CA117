#!/usr/bin/env python3

import sys

bests = {}

#def assign(item):
#	bests[line[0]] = line[1:]

names = []

for line in sys.stdin:
	line = line.strip().split()
	bests[line[0]] = line[1:]
	


print(bests)
best = max(bests.keys())
for k, v in bests.items():
	print(f'{k} =====> {v}')
	if k == best:
		names.append(v)

print(best)
print(names)