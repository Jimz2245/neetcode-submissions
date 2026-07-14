class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        res = nums[0]

        for num in nums[1:]:
            temp = curMax
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(temp * num, curMin * num, num)
            res = max(curMax, res)

        return res