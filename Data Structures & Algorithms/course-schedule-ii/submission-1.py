class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        path = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            indegree[crs] += 1
            path[pre].append(crs)

        res = []

        q = collections.deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            res.append(node)
            for crs in path[node]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs)

        for crs in range(numCourses):
            if indegree[crs] != 0:
                return []
        return res
        