class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        res = []

        def find(i):
            while parent[i] != i:
                i = parent[i]
            return i

        def union(a, b):
            nonlocal res
            rootA = find(a)
            rootB = find(b)
            if rootA == rootB:
                res = [a, b]
            else:
                parent[rootA] = rootB

        for a, b in edges:
            union(a, b)
        return res

        