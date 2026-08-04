class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}
        dp[0] = 0

        def dfs(i):
            for j in range(i + 1, i + nums[i] + 1):
                if j >= len(nums):
                    break
                if j in dp:
                    dp[j] = min(dp[j], dp[i] + 1)
                else:
                    dp[j] = dp[i] + 1

        for i in range(len(nums)):
            dfs(i)

        return dp[len(nums) - 1]

            