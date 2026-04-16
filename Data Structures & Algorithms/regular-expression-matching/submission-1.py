class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True

            if j == len(p):
                return False

            if i == len(s):
                return dfs(i, j+2) if j+1 < len(p) and p[j+1] == '*' else False

            if (i,j) in memo:
                return memo[(i,j)]

            if j+1 < len(p) and p[j+1] == '*':
                if dfs(i, j+2):
                    memo[(i,j)] = True
                    return memo[(i,j)]
                if (s[i] == p[j] or p[j] == '.') and dfs(i+1, j):
                    memo[(i,j)] = True
                    return memo[(i,j)]
            elif s[i] == p[j] or p[j] == '.':
                if dfs(i+1, j+1):
                    memo[(i,j)] = True
                    return memo[(i, j)]
            memo[(i,j)] = False
            return memo[(i, j)]
        return dfs(0,0)