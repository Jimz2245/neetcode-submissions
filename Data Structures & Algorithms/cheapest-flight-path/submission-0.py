class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = { i:[] for i in range(n)}
        for u, v, w in flights:
            adj[u].append((v, w))

        prices = [float('inf')] * n
        prices[src] = 0  # cost to reach source is 0

        q = deque([(src, 0)])  # (node, current_cost)

        for i in range(k + 1):
            for j in range(len(q)):
                curr, cost = q.popleft()
                for node, price in adj[curr]:
                    if (cost+price) < prices[node]:
                        prices[node] = cost + price
                        q.append((node, cost+price))

        if prices[dst] != float('inf'):
            return prices[dst]
        else:
            return -1

        

        