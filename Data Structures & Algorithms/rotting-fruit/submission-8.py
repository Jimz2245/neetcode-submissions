class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        mins = 0
        fresh = 0

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append([row, col])

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if row >= 0 and col >= 0 and row < rows and col < cols and grid[row][col] == 1:
                        q.append([row, col])
                        grid[row][col] = 2
                        fresh -= 1
            mins += 1

        return mins if fresh == 0 else -1

            


        
        
                
        

