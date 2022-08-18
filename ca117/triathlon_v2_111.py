#!/usr/bin/env python3

def sort_on(t):
    return t.name

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return f'Name: {self.name}\nID: {self.tid}'

class Triathlon(object):

    def __init__(self):
        self.d = {}

    def add(self, t):
        self.d[t.tid] = t

    def remove(self, tid):
        del(self.d[tid])

    def lookup(self, tid):
        if tid in self.d:
            return self.d[tid]
        return None

    def __str__(self):
        slist = [f'{t}' for t in sorted(self.d.values(), key=sort_on)]
        return '\n'.join(slist)
