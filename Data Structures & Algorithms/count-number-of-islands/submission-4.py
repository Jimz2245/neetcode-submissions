class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0

        def dfs(r, c):
            if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]) and grid[r][c] == "1":
                grid[r][c] = "#"

                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    count += 1

        return count


