class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            L = i + 1
            R = len(nums) - 1
            while L < R:
                if nums[L] + nums[R] > target:
                    R = R - 1
                elif nums[L] + nums[R] < target:
                    L = L + 1
                else:
                    l = [nums[i], nums[L], nums[R]]
                    ret.append(l)
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                            L += 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1
        return ret


            
