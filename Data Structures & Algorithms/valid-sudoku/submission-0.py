class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    rowSeen = board[row][col] + " in row " + str(row)
                    colSeen = board[row][col] + " in col " + str(col)
                    boxSeen = board[row][col] + " in square " +  str(((row // 3) * 3 + (col // 3)))
                    if rowSeen in seen or colSeen in seen or boxSeen in seen:
                        return False
                    else:
                        seen.add(rowSeen)
                        seen.add(colSeen)
                        seen.add(boxSeen)
        return True

        