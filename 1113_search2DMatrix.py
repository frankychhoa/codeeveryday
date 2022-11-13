class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ##binary search             
        
        def binarySearch(row,l,r):
            while l <= r:
                col = (l+r)//2
                #print(matrix[row][col])
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] < target:
                    l += 1
                elif matrix[row][col] > target:
                    r -= 1
            return False
        for i in range(len(matrix)):
            l,r = 0, len(matrix[0])-1
            if binarySearch(i,l,r) == True:
                return True
        return False