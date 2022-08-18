#!/usr/bin/env python3

import sys

def main():
    numbers = [int(n) for n in sys.stdin.readline().strip().split()]
    a, b, c = [str(n) for n in sorted(numbers)]
    d = {'A': a, 'B': b, 'C': c}
    order = sys.stdin.readline().strip()
    s = [d[c] for c in order]
    print(f'{" ".join(s)}')


if __name__ == '__main__':
    main()
