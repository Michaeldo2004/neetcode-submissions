class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if 0 > i or i >= len(grid) or 0 > j or j >= len(grid[0]) or grid[i][j] in {"0", '#'}:
                return
            
            grid[i][j] = "#"
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)

        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    c +=1
        return c
