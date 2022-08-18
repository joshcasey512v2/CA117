#!/usr/bin/env python3

import sys

atotal = []
etotal = []
ototal = []
itotal = []
utotal = []

for line in sys.stdin:
	words = line.lower().strip()
	atotal.append(words.count('a'))
	etotal.append(words.count('e'))
	ototal.append(words.count('o'))
	itotal.append(words.count('i'))
	utotal.append(words.count('u'))

print('e :', sum(etotal))
print('a :', sum(atotal))
print('o :', sum(ototal))
print('i :', sum(itotal))
print('u :', sum(utotal))