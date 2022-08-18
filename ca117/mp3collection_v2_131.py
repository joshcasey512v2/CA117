#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title, duration, artist):
        self.title = title
        self.duration = duration
        self.artist = artist

    def __str__(self):
        return f'Title: {self.title}\nBy: {", ".join(self.artist)}\nDuration: {self.duration}'

class MP3Collection(object):

    def __init__(self):
        self.d = {}

    def add(self, track):
        self.d[track.title] = track

    def get_mp3s_by_artist(self, artist):
        lis = []
        for self.artist in self.d.values():
            lis.append(self.artist)
        return len(lis) 
