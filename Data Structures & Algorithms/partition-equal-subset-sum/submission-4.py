class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        nums.sort()
        target = 0

        for num in nums:
            target += num

        if target%2 == 1:
            return False

        target = target/2

        dp = {0}

        for num in nums:
            for i in set(dp):
                if i + num == target:
                    return True
                else:
                    dp.add(i + num)

        return False