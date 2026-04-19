class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        q = deque()
        t_s = set()
        b_s = set()
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    q.append((i, j))
        
        while len(q) > 0:
            x, y = q.popleft()
            t_s.add((x, y))
            direction = [(1,0), (0, 1), (-1, 0), (0, -1)]
            for dirx, diry in direction:
                nx = x + dirx
                ny = y + diry
                if 0 <= nx < len(heights) and 0 <= ny < len(heights[0]) and (nx, ny) not in t_s and heights[x][y] <= heights[nx][ny]:
                    q.append((nx,ny))
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == len(heights)-1 or j == len(heights[0])-1:
                    q.append((i, j))
        
        while len(q) > 0:
            x, y = q.popleft()
            b_s.add((x, y))
            direction = [(-1,0), (0, 1), (1, 0), (0, -1)]
            for dirx, diry in direction:
                nx = x + dirx
                ny = y + diry
                if 0 <= nx < len(heights) and 0 <= ny < len(heights[0]) and (nx, ny) not in b_s and heights[x][y] <= heights[nx][ny]:
                    q.append((nx,ny))
        return list(b_s & t_s)
