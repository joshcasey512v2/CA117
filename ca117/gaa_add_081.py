#!/usr/bin/env python3

class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def __str__(self):
        return f'{self.goals} goal(s) and {self.points} point(s)'

    def __iadd__(self, other):
        self.goals += other.goals
        self.points += other.points
        return self

    def __add__(self, other):
        tg = self.goals + other.goals
        tp = self.points + other.points
        return Score(tg, tp)
