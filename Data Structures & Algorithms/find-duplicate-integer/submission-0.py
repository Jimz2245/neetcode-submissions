class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        set = []
        for num in nums:
            if num in set:
                return num
            else:
                set.append(num)
        return -1