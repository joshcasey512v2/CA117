#!/usr/bin/env python3

import sys

calc_memory = {}

def assign(item):
    if line[0] == 'def':
        calc_memory[line[1]] = int(line[2])

def calc(item):
    try:
        if line[0] == 'calc':
            math = line[1:]
            total = calc_memory[math[0]]
            for i in range(len(math)):
                if math[i] == '-':
                    total = total - calc_memory[math[i + 1]]
                if math[i] == '+':
                    total = total + calc_memory[math[i + 1]]
            for k, v in calc_memory.items():
                if v == total:
                    return f'{" ".join(math)} {k}'
        return f'{" ".join(math)} unknown'
    except KeyError:
        return f'{" ".join(math)} unknown'


for line in sys.stdin:
    try:
        line = line.strip().split()
        assign(line)
        if line[0] == 'calc':
            print(calc(line))
        if line[0] == 'clear':
            calc_memory.clear()
    except IndexError:
        print('Invalid Input')
