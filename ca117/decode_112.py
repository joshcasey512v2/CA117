#!/usr/bin/env python3

stdin = ['papapapa',
         'papapripikapa',
         'prepetty popolly',
'pepeteper pipipeper pipickeped apa pepeck opof pipickleped pepeppepers',
'jipimmy lopovepes sapally opobripiepen']

vowels = 'aeiou'

for line in stdin:
    make = ""
    i = 0
    while i < len(line):
        if line[i] in vowels:
            i = i + 2
        make = make + line[i]
        i = i + 1
    print(make.strip())
