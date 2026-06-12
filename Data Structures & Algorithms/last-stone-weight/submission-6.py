class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            first = -heapq.heappop(maxHeap)
            second = -heapq.heappop(maxHeap)
            res = first - second
            if res > 0:
                heapq.heappush(maxHeap, -res)
        if len(maxHeap) > 0:
            return -maxHeap[0]
        return 0