#!/usr/bin/env python3

import sys

table = {}


def sort(item):
    return item[1]


for lines in sys.stdin:
     nums = []
     lines = lines.strip().split(":")
     nums.append(lines[1])
     int_nums = (" ".join(nums).split(","))
     avg = [int(n) for n in int_nums]
     average = (sum(avg) / len(avg))
     table[lines[0]] = average


for k, v in sorted(table.items(), key=sort, reverse=True):
    print(f'{k}: {v:.2f}')
 