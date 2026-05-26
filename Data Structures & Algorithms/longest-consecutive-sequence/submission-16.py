class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0
        nums.sort()
        prev = 0

        for i in nums:
            if count == 0:
                count = count + 1
            else:
                if i == prev + 1:
                    count += 1
                elif i == prev:
                    prev = i
                    continue
                else:
                    maxCount = max(maxCount, count)
                    count = 1
            prev = i
        
        maxCount = max(maxCount, count)

        return maxCount
        