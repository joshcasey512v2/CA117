#!/usr/bin/env python3

import sys

vowels = ["a", "e", "i", "o", "u"]
end1 = ["x", "s", "z", "o"]
end2 = ["ch", "sh"]

def plural(s):
    if s[len(s) - 1] in end1 or s[len(s) - 2:] in end2:
        print(s + "es")
    elif s[len(s) - 2] not in vowels and s[len(s) - 1] == "y":
        print(s[:len(s) - 1] + "ies")
    elif s[len(s) - 1] == "f":
        print(s[:len(s) - 1] + "ves")
    elif s[len(s) - 2:] == "fe":
        print(s[:len(s) - 2] + "ves")
    else:
        print(s + "s")


for line in sys.stdin:
    s = line.strip()
    p = plural(s)
