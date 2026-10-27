"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0: return True
        
        intervals = sorted(intervals, key=lambda x: x.start, reverse=False)

        t0, t1 = intervals[0].start, intervals[0].end
        for interval in intervals[1:]:
            newt0, newt1 = interval.start, interval.end
            if t1 > newt0: return False
            else: t1 = newt1

        return True
