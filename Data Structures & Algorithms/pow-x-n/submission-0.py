class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n > 0:
            for i in range(n):
                res *= x
        if n < 0:
            for i in range(n * -1):
                res /= x
        return res
        