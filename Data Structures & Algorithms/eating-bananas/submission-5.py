class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 1
        r = piles[len(piles) - 1]
        minEat = piles[len(piles) - 1]
        while l < r:
            k = int((l+r)/2)
            total = 0
            for i in range(len(piles)):
                total += math.ceil(piles[i]/k)
            if total <= h:
                minEat = min(minEat, k)
                r = k
            else:
                l = k+1
        return minEat

        