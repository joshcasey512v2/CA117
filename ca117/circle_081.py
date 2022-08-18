#!/usr/bin/env python3


class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def midpoint(self, other):
        xm = (self.x + other.x) / 2
        ym = (self.y + other.y) / 2
        return Point(xm, ym)

    def __str__(self):
        return f'({self.x:.01f}, {self.y:.01f})'

class Circle(object):

    def __init__(self, centre=None, radius=1):
        self.radius = radius
        self.centre = Point() if centre is None else centre

    def __str__(self):
        line = []
        line.append(f'Centre: {self.centre}')
        line.append(f'Radius: {self.radius}')
        return "\n".join(line)
