class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) -1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[m][0] == target: return True

            if matrix[m][0] < target:
                l = m + 1
            else:
                r = m - 1

        
        index = r

        l = 0
        r = len(matrix[index]) -1

        while l <= r:
            m = l + (r - l) // 2
            if matrix[index][m] == target: return True

            if matrix[index][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False