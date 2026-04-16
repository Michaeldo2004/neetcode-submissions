class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        t = 0
        o = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    o += 1
        while(len(q) > 0):
            flag = False
            for _ in range(len(q)):
                x, y = q.popleft()
                direction = [(0,1), (1,0), (-1,0), (0, -1)]
                for dirx, diry in direction:
                    adjx = x + dirx
                    adjy = y + diry
                    if 0 <= adjx < len(grid) and 0 <= adjy < len(grid[0]) and grid[adjx][adjy] == 1:
                        grid[adjx][adjy] = 2
                        q.append((adjx, adjy))
                        flag = True
                        o -=1
            t += 1 if flag else 0
        return t if o == 0 else -1
        