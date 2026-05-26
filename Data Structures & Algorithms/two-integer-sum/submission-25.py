class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i = 0 
        while(i < len(nums)):
            diff = target - nums[i]
            if (diff in seen):
                return[seen[diff], i]
            seen[nums[i]] = i
            i += 1