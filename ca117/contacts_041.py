#!/usr/bin/env python3

import sys

phonebook = {}
names = []


with open(sys.argv[1], 'r') as f:
    for lines in f:
        book = lines.strip().split()
        phonebook[book[0]] = book[1]

for name in sys.stdin:
    name = name.strip()
    names.append(name)

for i in range(len(names)):
    if names[i] in phonebook:
        print("Name:", names[i])
        print("Phone:", phonebook[names[i]])
    else:
        print("Name:", names[i])
        print("No such contact")
