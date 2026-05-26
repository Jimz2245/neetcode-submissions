class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        mostWater = 0
        Lpoint = 0
        Rpoint = len(heights) - 1
        while Lpoint < Rpoint:
            mostWater = max(min(heights[Lpoint], heights[Rpoint]) * (Rpoint - Lpoint), mostWater)
            if heights[Lpoint] < heights[Rpoint]:
                Lpoint = Lpoint + 1
            else:
                Rpoint = Rpoint - 1
        return mostWater

        