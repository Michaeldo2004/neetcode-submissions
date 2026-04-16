"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [i.start for i in intervals]
        starts.sort()
        ends = [i.end for i in intervals]
        ends.sort()
        s = 0
        e = 0
        maxC = 0
        c = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                s += 1
                c += 1
                maxC = max(maxC, c)
            else:
                e += 1
                c -=1
        return maxC


        