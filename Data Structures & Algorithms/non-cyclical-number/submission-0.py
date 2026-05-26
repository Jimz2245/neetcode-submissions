class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        temp = 0
        while temp != 1:
            temp = 0
            while n != 0:
                temp += (n % 10) ** 2
                n //= 10
            if temp in seen:
                return False
            seen.add(temp)
            n = temp
        return True
        