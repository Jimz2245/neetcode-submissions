class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqA = {}
        freqB = {}
        
        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            freqA[s1[i]] = 1 + freqA.get(s1[i], 0)
            freqB[s2[i]] = 1 + freqB.get(s2[i], 0)
        
        l = 0 
        r = len(s1) - 1

        if(freqA == freqB):
            return True

        while(r < len(s2) - 1):
            freqB[s2[l]] -= 1
            if freqB[s2[l]] == 0:
                del freqB[s2[l]]
            l += 1

            r += 1
            freqB[s2[r]] = 1 + freqB.get(s2[r], 0)

            if(freqA == freqB):
                return True


        return False
        
        
        
            
            

            
        