#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title, duration, artist):
        self.title = title
        self.duration = duration
        self.artist = artist

    def __str__(self):
        return f'Title: {self.title}\nBy: {", ".join(self.artist)}\nDuration: {self.duration}'
