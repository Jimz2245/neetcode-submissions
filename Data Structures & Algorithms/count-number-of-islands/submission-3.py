class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        seen = set()


        def dfs(r, c):
            if (r >= 0 and c >= 0 and r < rows and c < cols and grid[r][c] != "#" and grid[r][c] != "0"):  
 
                grid[r][c] = "#"

                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    count += 1

        return count
