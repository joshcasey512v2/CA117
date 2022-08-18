#!/usr/bin/env python3

sys.stdin = ['Abe', 'Max', 'Mary', 'Jane', 'Polly', 'Timmy']

line = [line.strip() for line in sys.stdin]

fh = line[::2]
sh = line[1::2]

print('\n'.join(fh + sh[::-1]))
