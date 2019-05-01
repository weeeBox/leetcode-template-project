# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    @staticmethod
    def from_list(intervals):
        result = []
        for start, end in intervals:
            result.append(Interval(start, end))
        return result

    def __eq__(self, other):
        if self is other:
            return True

        elif type(self) != type(other):
            return False
        else:
            return self.start == other.start and self.end == other.end

    def __str__(self):
        return "[%d, %d]" % (self.start, self.end)

    def __repr__(self):
        return self.__str__()
