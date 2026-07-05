class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        minHeap = [(grid[0][0], 0, 0)]
        target = (len(grid) - 1, len(grid[0]) - 1)
        seen = {(0, 0)}
        res = 0


        def heapAdd(x, y):
            if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]) and (x,y) not in seen:
                heapq.heappush(minHeap, (grid[x][y], x, y))
                seen.add((x, y))

        while minHeap:
            node, x, y = heapq.heappop(minHeap)
            res = max(node, res)
            if (x, y) == target:
                return res
            heapAdd(x - 1, y)
            heapAdd(x + 1, y)
            heapAdd(x, y - 1)
            heapAdd(x, y + 1)

        return res
        
                

            
