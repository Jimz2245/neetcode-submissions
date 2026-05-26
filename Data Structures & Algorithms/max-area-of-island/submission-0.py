class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if row >= 0 and row < rows and col >= 0 and col < cols and grid[row][col] == 1:
                grid[row][col] = 0
                return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) +  dfs(row, col - 1)
            return 0
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(dfs(r, c), res)
        
        return res

        