# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def as_list(self):
        return [self.start, self.end]

    def __str__(self):
        return "[%d, %d]" % (self.start, self.end)