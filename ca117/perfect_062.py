#!/usr/bin/env python3

import sys

def sum_factors(num):
	nums = [n for n in range(1, (num // 2) + 1)]
	for i in range(len(nums)):
		if num % nums[i] == 0:
			factors.append(nums[i])
	return sum(factors)


def is_perfect(num):
	return num == sum_factors(num)


for line in sys.stdin:
	line = line.strip()
	print(is_perfect(int(line)))
