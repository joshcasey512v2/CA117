#!/usr/bin/env python3

import sys

def isprime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


for line in sys.stdin:
    s = line.strip()
    n = int(s)
    a = []
    for num in range(1, n + 1):
        if isprime(num):
            a.append(num)
    print("Primes:", a)
