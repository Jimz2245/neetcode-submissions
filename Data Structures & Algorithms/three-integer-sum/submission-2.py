class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = - nums[i]
            L = i + 1
            R = len(nums) - 1
            while L < R:
                num = nums[L] + nums[R]
                if(num == target):
                    res.append([nums[i], nums[L], nums[R]])
                    L+=1
                    R-=1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    while L< R and nums[R] == nums[R+1]:
                        R -= 1
                elif(num < target):
                    L += 1
                else:
                    R -= 1
        return res