from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))

        while (len(q) > 0):
            x, y = q.popleft()
            direction = [(0,1), (1,0), (-1,0), (0, -1)]
            for dirx, diry in direction:
                adjx = x + dirx
                adjy = y + diry
                if 0 <= adjx < len(grid) and 0 <= adjy < len(grid[0]) and grid[adjx][adjy] == 2147483647:
                    grid[adjx][adjy] = 1 + grid[x][y]
                    q.append((adjx, adjy))
        


