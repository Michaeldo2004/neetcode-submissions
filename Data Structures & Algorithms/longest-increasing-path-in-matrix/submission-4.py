class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}

        def dfs(i, j):
            if i >= len(matrix) or j >= len(matrix[0]) or i < 0 or j < 0:
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]

            valid = []
            direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for ni, nj in direction:
                ti = i + ni
                tj = j + nj
                if 0 <= ti < len(matrix) and 0 <= tj < len(matrix[0]) and matrix[ti][tj] > matrix[i][j]:
                    valid.append((ti, tj))
                
            memo[(i,j)] = 1 + max(dfs(a, b) for a,b in valid) if valid else 1
            return memo[(i,j)]
        n = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                n = max(n, dfs(i,j))
        return n