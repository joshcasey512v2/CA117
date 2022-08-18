#!/usr/bin/env python3

import sys

from string import ascii_lowercase

for line in sys.stdin:
    missing = []
    words = line.lower().strip()
    for c in ascii_lowercase:
        if c not in words:
            missing.append(c)
    if len(missing) == 0:
        print("pangram")
    else:
        print("missing", "".join(missing))
