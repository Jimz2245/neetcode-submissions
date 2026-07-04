class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        minHeap = [(0, 0)]
        res = 0

        def manhattan(x, y):
            return (abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1]))
            
        while minHeap:
            distance, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            res += distance
            visited.add(node)
            for i in range(len(points)):
                if i not in visited:
                    heapq.heappush(minHeap, (manhattan(node, i), i))

        return res
                



                
        