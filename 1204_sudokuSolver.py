class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        arr=[]
        col_start=0
        row_start=0
        to_add=[]
        while row_start < 9:
            col_start=0
            while col_start < 9:
                sub=[]
                for i in range(0,3):
                    #for j in range(0,3):\
                    col=col_start
                    for j in range(3):
                        sub.append((i+row_start,col+j))
                arr.append(sub)
                col_start += 3
            row_start += 3
        d={}
        for i in arr:
            for j in i:
                d[j] = i
        ##to_add
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    to_add.append((i, j))
        def isValid(row,col,n):
            #check duplicate
            ##check row
            for index,i in enumerate(board[row]):
                if i == str(n) and index != col:
                    return False
            ##check col
            for i in range(9):
                if board[i][col] == str(n) and i != row:
                    return False
            ##check square
            sq=d[(int(row),int(col))]
            for i in sq:
                if board[i[0]][i[1]] == str(n) and row != i[0] and col != i[1]:
                    return False
            return True
        def backTracking():
            if not to_add:
                return True
            i, j = to_add.pop()
            for n in range(1,10):
                board[i][j] = str(n)
                if isValid(i,j,n) == True:
                    if backTracking():
                        return True
                board[i][j] = "."
            to_add.append((i, j))
            return False
        backTracking()