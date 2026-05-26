class Solution:
    def trap(self, height: List[int]) -> int:    
        left = 0
        right = len(height) - 1
        maxLeft = height[left]
        maxRight = height[right]
        water = 0
        while(left < right):
            if(maxLeft < maxRight):
                left += 1
                if(height[left] > maxLeft):
                    maxLeft = height[left]
                else:
                    water += min(maxLeft, maxRight) - height[left] 
            else:
                right -= 1
                if(height[right] > maxRight):
                    maxRight = height[right]
                else:
                    water += min(maxLeft, maxRight) - height[right] 
        return water
                





        
            
        