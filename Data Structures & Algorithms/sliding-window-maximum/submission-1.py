class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = {}
        l = 0
        for r in range(len(nums)):
            window[nums[r]] = 1 + window.get(nums[r], 0)
            if(r >= k - 1):
                res.append(max(window.keys()))
                window[nums[l]] -= 1
                if window[nums[l]] == 0:
                    del window[nums[l]]
                l += 1
        return res































            


        