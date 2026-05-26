class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        ret = [-1, -1]
        resLen = float("infinity")

        freqA = {}
        freqB = {}

        for i in t:
            freqA[i] = 1 + freqA.get(i, 0)

        have = 0
        need = len(freqA)
        
        l = 0

        for r in range(len(s)):
            c = s[r]
            freqB[c] = 1 + freqB.get(c, 0)

            if(c in freqA and freqB[c] == freqA[c]):
                have += 1

            while have == need:
                if(r-l+1 < resLen):
                    ret = [l, r]
                    resLen = (r - l + 1)
                freqB[s[l]] -= 1
                if (s[l] in freqA and freqB[s[l]] < freqA[s[l]]):
                    have -=1
                l += 1
        l, r = ret
        return s[l:r+1] if resLen != float("infinity") else ""




        