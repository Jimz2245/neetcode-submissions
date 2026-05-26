class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        while r < len(s2):
            if sorted(s2[l:(r + 1)]) == sorted(s1):
                return True
            if r < len(s1)-1:
                r += 1
            else:
                r+=1
                l+=1 
        return False
            

            
        