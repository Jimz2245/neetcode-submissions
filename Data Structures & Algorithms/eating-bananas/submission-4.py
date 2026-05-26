class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = max(piles)
        while left <= right:
            hours = 0
            per = (right + left)// 2
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / per)
            if hours <= h:
                res = min(res, per)
                right = per - 1
            else:
                left = per + 1
        return res
            
            


        