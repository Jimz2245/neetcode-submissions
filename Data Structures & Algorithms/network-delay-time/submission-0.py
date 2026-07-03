class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        seen = set()
        adj = {i:[] for i in range(1, n + 1)}
        res = 0
        minHeap = [(0, k)]

        for i in range(len(times)):
            adj[times[i][0]].append((times[i][1], times[i] [2]))

        while minHeap:
            distance, node = heapq.heappop(minHeap)
            if node not in seen:
                res = max(res, distance)
                seen.add(node)
                for neighbor, b in adj[node]:
                    if neighbor not in seen:
                        heapq.heappush(minHeap, ((distance + b), neighbor))

        return res if len(seen) == n else -1