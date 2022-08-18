#!/usr/bin/env python3

class Meeting(object):

    def __init__(self, hour, minute, duration):
        self.hour = hour
        self.minute = minute
        self.duration = duration

    def __str__(self):
        return f'{self.hour:02}:{self.minute:02} ({self.duration} minutes)'

class Schedule(object):

    def __init__(self):
        self.d = {}

    def add(self, meeting):
        self.d[meeting.hour] = meeting

    def __str__(self):
        slist = []
        slist.append('Schedule')
        slist.append('--------')
        for k, v in sorted(self.d.items()):
            slist.append('{}'.format(v))
        slist.append('Meetings today: ' + str(len(self.d)))
        return '\n'.join(slist)
