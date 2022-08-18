#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.d = {}

    def __str__(self):
        return f'Name: {self.name}\nID: {self.tid}\nRace time: {sum(self.d.values())}'

    def add_time(self, sport, time):
        self.d[sport] = time

    def get_time(self, sport):
        return self.d[sport]
