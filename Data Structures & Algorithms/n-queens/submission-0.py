class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        r = []
        col_seen = set()
        col_list = []
        diag_seen = set()
        r_diag_seen = set()
        def dfs(row):
            if row == n:
                r.append(["." * c + "Q" + "." * (n - c -1) for c in col_list])
                return

            for col in range(n):
                if col not in col_seen and row - col not in diag_seen and row + col not in r_diag_seen:
                    col_seen.add(col)
                    col_list.append(col)
                    diag_seen.add(row-col)
                    r_diag_seen.add(row+col)

                    dfs(row+1)

                    col_seen.discard(col)
                    col_list.pop()
                    diag_seen.discard(row-col)
                    r_diag_seen.discard(row+col)
            
        dfs(0)
        return r


            