class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        res = 1
        for num in range(n - 1):
            temp = res
            res += prev
            prev = temp
        return res