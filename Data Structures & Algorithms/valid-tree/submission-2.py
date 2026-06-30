class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adjList = {i:[] for i in range (n)}

        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)

        seen = {0}
        q = collections.deque([0])

        while q:
            node = q.popleft()
            for pre in adjList[node]:
                if pre not in seen:
                    q.append(pre)
                    seen.add(node)
            seen.add(node)

        return len(seen) == n