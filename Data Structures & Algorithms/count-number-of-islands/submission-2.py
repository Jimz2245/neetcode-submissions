class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(row, col):
            if row < rows and row >= 0 and col < cols and col >= 0 and grid[row][col] == "1"  and (row, col) not in seen:
                seen.add((row, col))
                grid[row][col] = "0"
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        
        return islands


        