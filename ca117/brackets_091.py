#!/usr/bin/env python3

def matcher(line):

    class Stack(object):

        def __init__(self):
            self.list = []

        def pop(self):
            return self.list.pop()

        def push(self, p):
            return self.list.append(p)

        def top(self):
            return self.list[-1]

        def is_empty(self):
            return len(self.list) == 0

        def __len__(self):
            return len(self.list)

    dic = {')': '(', ']': '[', '}': '{'}

    s = Stack()

    try:
        for c in line:
            if c in dic.values():
                s.push(c)

            if c in dic:
                if dic[c] != s.pop():
                    return False
    except IndexError:
        return False

    return s.is_empty()
