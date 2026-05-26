class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        Lpoint = 0
        Rpoint = len(s) - 1
        while Lpoint < Rpoint:
            if not s[Lpoint].isalnum():
                Lpoint = Lpoint + 1
                continue
            if not s[Rpoint].isalnum():
                Rpoint = Rpoint - 1
                continue
            if s[Lpoint] != s[Rpoint]:
                return False
            Lpoint = Lpoint + 1
            Rpoint = Rpoint - 1
        return True