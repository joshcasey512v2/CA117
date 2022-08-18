#!/usr/bin/env python3

def reverse_list(l):
    if len(l) == 1:
        return [l[0]]
    if len(l) == 0:
        return []
    return [l[-1]] + reverse_list(l[:-1])
