class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mostWater = 0
        Lpoint = 0
        Rpoint = len(heights) - 1
        while Lpoint < Rpoint:
            mostWater = max(mostWater, min(heights[Lpoint], heights[Rpoint]) * (Rpoint - Lpoint))
            if heights[Lpoint] < heights[Rpoint]:
                Lpoint = Lpoint + 1
            else:
                Rpoint = Rpoint - 1
        return mostWater

        