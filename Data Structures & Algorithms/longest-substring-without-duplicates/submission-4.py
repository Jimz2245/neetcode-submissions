class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        L = 0
        R = 0
        sub = set()
        while R < len(s):
            if s[R] in sub:
                sub.remove(s[L])
                L += 1
            else:
                sub.add(s[R])
                if len(sub) > count:
                    count = len(sub)
                R += 1
        return count

        