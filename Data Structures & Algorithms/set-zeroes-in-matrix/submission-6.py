class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r_z = False
        for r_idx, row in enumerate(matrix):
            for c_idx, num in enumerate(row):
                if num == 0:
                    #left + topmost row = target rows to modify
                    if r_idx > 0:
                        matrix[r_idx][0] = 0
                    else:
                        r_z = True
                    matrix[0][c_idx] = 0

        for r_idx, row in enumerate(matrix[1:]):
            for c_idx, _ in enumerate(row[1:]):
                if matrix[r_idx+1][0] == 0 or matrix[0][c_idx+1] == 0:
                    matrix[r_idx+1][c_idx+1] = 0
        
        if matrix[0][0] == 0:
            for r_idx, row in enumerate(matrix):
                matrix[r_idx][0] = 0
        if r_z:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0