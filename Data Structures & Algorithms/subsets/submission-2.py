class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def backtrack(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            backtrack(i+1, curr)
            curr.pop()
            backtrack(i+1, curr)
        
        backtrack(0, curr)
        return res






































        res = [[]]
        for i in range(len(nums)):
            for j in range(len(res)):
                curr = res[j] + [nums[i]]
                res.append(curr)
        return res
