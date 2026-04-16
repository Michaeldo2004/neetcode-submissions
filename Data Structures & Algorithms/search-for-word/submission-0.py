class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        def dfs(i, j, string):
            if string == word:
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return
            if board[i][j] != word[len(string)]:
                return
            curr = board[i][j]
            board[i][j] = "#"
            rst = dfs(i-1, j, string+curr) or dfs(i+1, j, string+curr) or dfs(i, j+1, string+curr) or dfs(i, j-1, string+curr)
            board[i][j] = curr
            return rst

        
        for row in range(len(board)):
            for idx in range(len(board[row])):
                if dfs(row, idx, ""):
                    return True
        return False
