class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            elif intervals[i][0] <= newInterval[1]:
                newInterval = [min(intervals[i][0], newInterval[0]), max(newInterval[1], intervals[i][1])]
            else:
                res.append(newInterval)
                for j in range(i, len(intervals)):
                    res.append(intervals[j])
                break
                
        if newInterval not in res:
            res.append(newInterval)

        return res


            
            