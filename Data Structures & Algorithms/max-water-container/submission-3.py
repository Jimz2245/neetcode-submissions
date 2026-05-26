class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0
        L = 0
        R = len(heights) - 1
        while L < R:
            most = max(most, min(heights[L], heights[R]) * (R - L))
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return most

        