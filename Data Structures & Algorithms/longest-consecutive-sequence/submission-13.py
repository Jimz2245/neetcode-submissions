class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ret = 0
        count = 0
        nums.sort()
        print(nums)
        prev = 0
        for i in nums:
            if count == 0:
                count = count + 1
            else:
                if i == prev + 1:
                    count = count + 1
                elif i == prev:
                    prev = i
                    continue
                else:
                    if count > ret:
                        ret = count
                    count = 1 
            print(count) 
            prev = i

        if count > ret:
            ret = count

        return ret

        