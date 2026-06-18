class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums)):
            for j in range(len(res)):
                curr = res[j] + [nums[i]]
                res.append(curr)
        return res
