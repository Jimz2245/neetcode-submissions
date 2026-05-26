class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0
        while(left < right):
            maxArea = max(min(heights[left], heights[right]) * (right - left), maxArea)
            if(heights[left] < heights[right]):
                prevLeft = heights[left]
                left+=1
                while(heights[left] < prevLeft and left < right):
                    left += 1
            else:
                prevRight = heights[right]
                right-=1
                while(heights[right] < prevRight and left < right):
                    right -= 1
        return maxArea

            
        