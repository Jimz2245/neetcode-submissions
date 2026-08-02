class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {}
        dp[0] = True

        for i in range(len(nums)):
            if dp.get(i, False):
                for j in range(i + 1, i + nums[i] + 1):
                    dp[j] = True
        
        return dp.get(len(nums) - 1, False)
        

        