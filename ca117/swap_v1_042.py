#!/usr/bin/env python3

def swap_keys_values(dic):
    a = []
    b = []
    new_dict = {}
    for k, v in dic.items():
        a.append(k)
        b.append(v)
    for i in range(len(a)):
        new_dict[b[i]] = a[i]
    return new_dict

"""
better way
new_dict = {v: k for k, v in dict}