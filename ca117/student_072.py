#!/usr/bin/env python3

class Student(object):

    def __init__(self, sid, name, modlist=None):
        self.sid = sid
        self.name = name
        self.modlist = modlist
        if modlist is None:
            self.modlist = []

    def add_module(self, other):
        self.modlist.append(other)

    def del_module(self, other):
        self.modlist.pop(other)

    def __str__(self):
        return f'ID: {self.sid}\nName: {self.name}\nModules: {", ".join(self.modlist)}'
