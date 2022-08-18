#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.d = {}
        self.tot = 0

    def __str__(self):
        return f'Name: {self.name}\nID: {self.tid}\nRace time: {self.tot}'

    def add_time(self, sport, time):
        self.d[sport] = time
        self.tot += time

    def get_time(self, sport):
        return self.d[sport]

    def __eq__(self, other):
        return self.tot == other.tot

    def __gt__(self, other):
        return self.tot > other.tot
