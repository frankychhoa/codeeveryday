class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for n in range(len(matrix[0])):
            i1, i2 = 0, 0+1
            j1, j2 = n, n+1
            while i2 < len(matrix) and j2 < len(matrix[0]):

                if matrix[i1][j1] != matrix[i2][j2]:
                    return False
                i2 += 1
                j2 += 1
        for n in range(len(matrix)):
            i1, i2 = n, n+1
            j1, j2 = 0, 0+1
            while i2 < len(matrix) and j2 < len(matrix[0]):
                if matrix[i1][j1] != matrix[i2][j2]:
                    return False
                i2 += 1
                j2 += 1
        return True