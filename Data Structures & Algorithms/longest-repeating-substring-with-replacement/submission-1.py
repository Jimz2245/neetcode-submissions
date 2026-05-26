class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ret = 0
        freq = {}
        l = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0) #add 1 to the hashmap location or make one if doesnt exist
            
            if (r - l + 1) - max(freq.values()) > k: #amount of replacements is greater than skips
                freq[s[l]] -= 1 #slide the left pointer down
                l += 1
            ret = max(ret, r-l + 1)
        return ret





            