#!/usr/bin/env python3

import sys

def load_contacts(filename):
    d = {}
    with open(filename, 'r') as fin:
        for line in fin:
            name, phone, email = line.strip().split()
            d[name] = (phone, email)
    return d


def main():
    d = load_contacts(sys.argv[1])
    for line in sys.stdin:
        name = line.strip()
        print(f'Name: {name:s}')
        if name in d:
            print(f'Phone: {d[name][0]:s}')
            print(f'Email: {d[name][1]:s}')
        else:
            print('No such contact')


if __name__ == '__main__':
    main()
