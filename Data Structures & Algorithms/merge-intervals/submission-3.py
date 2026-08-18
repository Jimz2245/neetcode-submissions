class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])

        for i in range(len(intervals)):
            if len(res) > 0 and res[len(res) - 1][1] >= intervals[i][0]:
                res[len(res) - 1] = [res[len(res) - 1][0], max(res[len(res) - 1][1], intervals[i][1])]
                continue
            else:
                res.append(intervals[i])

        return res
                