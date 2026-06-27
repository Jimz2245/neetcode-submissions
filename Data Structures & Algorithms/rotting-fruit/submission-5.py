class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        mins = 0

        def bfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return
            else:
                grid[r][c] = 2
                q.append([r, c])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)

            if q:
                mins += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return mins
                
        

