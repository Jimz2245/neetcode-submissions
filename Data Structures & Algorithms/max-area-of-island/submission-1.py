class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r >= 0 and c >= 0 and r < rows and c < cols and grid[r][c] != 0:
                grid[r][c] = 0
                return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            return 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, dfs(row, col))
        
        return maxArea