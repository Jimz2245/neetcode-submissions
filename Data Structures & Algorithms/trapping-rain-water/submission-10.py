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
                if height[L] > Lmax:
                    Lmax = height[L]
                else:
                    sum += (min(Lmax, Rmax) - height[L])
            else:
                R -= 1
                if height[R] > Rmax:
                    Rmax = height[R]
                else:
                    sum += (min(Lmax, Rmax) - height[R])
        return sum
        


        