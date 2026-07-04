class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)

        for src in adj:
            adj[src].sort()

        res = []

        def dfs(node):
            while adj[node]:
                dst = adj[node].pop(0)
                dfs(dst)
            res.append(node)

        dfs("JFK")
        
        return res[::-1]