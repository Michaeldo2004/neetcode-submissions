class Solution:
    def solve(self, board: List[List[str]]) -> None:
        seen = set()


        q = deque()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if i in {0, len(board)-1} or j in {0, len(board[0])-1}:
                    if board[i][j] == "O":
                        q.append((i,j))
        

        while len(q) > 0:
            x, y = q.popleft()

            seen.add((x,y))

            dir = [(0,1), (0,-1), (1,0), (-1,0)]

            for dx, dy in dir:
                dirx = x + dx
                diry = y + dy

                if 0 <= dirx < len(board) and 0 <= diry < len(board[0]) and board[dirx][diry] == "O" and (dirx, diry) not in seen:
                    q.append((dirx, diry))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i,j) not in seen:
                    board[i][j] = "X"

            
