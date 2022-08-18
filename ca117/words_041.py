#!/usr/bin/env python3

import sys

from string import punctuation

word_count = {}

for line in sys.stdin:
	words = line.lower().strip().split()
	for i in range(len(words)):
		for c in words[i]:
			if c in punctuation:
				words[i] = words[i].replace(c, '')
		count = words.count(words[i])
		word_count[words[i]] = count


#word_count = sorted(word_count)

for (k, v) in sorted(word_count.items()):
	print(f'{k} : {v}')
	