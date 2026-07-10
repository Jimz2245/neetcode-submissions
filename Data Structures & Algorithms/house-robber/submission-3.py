class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        maxVal = nums[len(nums) - 1]

        for i in range(len(nums) - 3, -1, -1):
            nums[i] += maxVal
            maxVal = max(maxVal, nums[i+1])
        
        return max(nums[0], nums[1])