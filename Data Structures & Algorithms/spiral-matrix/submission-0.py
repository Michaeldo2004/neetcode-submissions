class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l = 0
        u = 0
        r = len(matrix[0])
        d= len(matrix)
        path = []
        while l < r and u < d:
            for i in range(l, r):
                path.append(matrix[u][i])
            u += 1

            for i in range(u, d):
                path.append(matrix[i][r-1])
            r -=1
            if u < d:
                for i in range(r-1, l-1, -1):
                    path.append(matrix[d-1][i])
                d -=1
            if l < r:
                for i in range(d-1, u-1, -1):
                    path.append(matrix[i][l])
                l +=1
        return path
