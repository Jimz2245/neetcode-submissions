class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        prev = intervals[0][1]
        count = -1

        intervals.sort(key = lambda x: x[0])
        for i in intervals:
            if i[0] < prev:
                prev = min(prev, i[1])
                count += 1
            else:
                prev = i[1]
            
        return count