"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        end = []
        intervals.sort(key = lambda x: x.start)

        for interval in intervals:
            if end and end[0] <= interval.start:
                heapq.heappop(end)
            heapq.heappush(end, interval.end)
        
        return len(end)

        