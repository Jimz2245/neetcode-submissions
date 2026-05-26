class Solution:
    def trap(self, height: List[int]) -> int:       
        L = 0
        Lmax = height[L]   
        R = len(height) - 1
        Rmax = height[R] 
        sum = 0
        while L < R:
            if Lmax < Rmax:
                L += 1
                diff = (min(Lmax, Rmax) - height[L])
                if diff > 0:
                    sum += diff
                if height[L] > Lmax:
                    Lmax = height[L]
            else:
                R -= 1
                diff = (min(Lmax, Rmax) - height[R])
                if diff > 0:
                    sum += diff
                if height[R] > Rmax:
                    Rmax = height[R]
        return sum





        
            
        