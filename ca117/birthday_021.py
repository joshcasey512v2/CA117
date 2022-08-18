#!/usr/bin/env python3

import calendar
import sys

for line in sys.stdin:
    s = line.strip().split()
    d = (calendar.weekday(int(s[2]), int(s[1]), int(s[0])))
    if d == 0:
        print("You were born on a Monday and Monday's child is fair of face.")
    if d == 1:
        print("You were born on a Tuesday and Tuesday's child is full of grace.")
    if d == 2:
        print("You were born on a Wednesday and Wednesday's child is full of woe.")
    if d == 3:
        print("You were born on a Thursday and Thursday's child has far to go.")
    if d == 4:
        print("You were born on a Friday and Friday's child is loving and giving.")
    if d == 5:
        print("You were born on  a Satday and Saturday's child works hard for a living.")
    if d == 6:
        print("You were born on a Sunday and Sunday's child is fair and wise and good in every way.")
