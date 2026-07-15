class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 1
        
        for i in range(1, len(nums)):
            addi = 0
            for j in range(0, i + 1):
                if nums[j] < nums[i]:
                    addi = max(addi, dp[j])
            dp[i] += addi
            res = max(res, dp[i])

        return res

        