class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Hashset = set()
        for num in nums:
            if (num in Hashset):
                return True
            Hashset.add(num)
        return False