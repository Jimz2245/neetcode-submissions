class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        res = 0

        connected = {i:[] for i in range(n)}

        for i, j in edges:
            connected[i].append(j)
            connected[j].append(i)

        q = collections.deque()

        for i in range(n):
            if i in seen:
                continue
            else:
                q.append(i)
                seen.add(i)
                while q:
                    node = q.popleft()
                    for child in connected[node]:
                        if child not in seen:
                            q.append(child)
                            seen.add(child)
                res += 1

        return res

        