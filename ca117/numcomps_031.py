#!/usr/bin/env python3

import sys


def mul_3(s):
    return [n for n in range(1, s + 1) if n % 3 == 0]

def sqr_3(s):
    return [n * n for n in range(1, s + 1) if n % 3 == 0]

def mul_4(s):
    return [n * 2 for n in range(1, s + 1) if n % 4 == 0]

def mul_4or3(s):
    return [n for n in range(1, s + 1) if n % 4 == 0 or n % 3 == 0]

def mul_4and3(s):
    return [n for n in range(1, s + 1) if n % 4 == 0 and n % 3 == 0]


for s in sys.stdin:
    print("Multiples of 3:", mul_3(int(s)))
    print("Multiples of 3 squared:", sqr_3(int(s)))
    print("Multiples of 4 doubled:", mul_4(int(s)))
    print("Multiples of 3 or 4:", mul_4or3((int(s))))
    print("Multiples of 3 and 4:", mul_4and3((int(s))))
