#!/usr/bin/env python3

import sys

no_qu = []

for line in sys.stdin:
	words = line.strip()
	if 'quq' in words:
		no_qu.append(words)
	if 'qu' not in words:
		no_qu.append(words)

print("Words with q but no u:", no_qu)