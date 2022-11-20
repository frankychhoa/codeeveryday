class Solution:
    def __init__(self):
        self.res = 0
    def totalNQueens(self, n: int) -> int:
        
        def placeQueen(row,col,board):
            b = copy.deepcopy(board)
            print("place")
            #print(row)
            #print(col)
            #print(b)
            b[row][col] = False
            l,r = col-1,col+1
            up,down = row-1,row+1
            while l >= 0:
                b[row][l] = False
                l -= 1
            while r < n:
                b[row][r] = False
                r+=1
            #print(b)
            while up >= 0:
                b[up][col]=False
                up -= 1
            while down < n:
                b[down][col]=False
                down += 1
            #print(b)
            #print("lrud")
            lUp_left,lUp_up, rUp_right, rUp_up = col-1, row-1, col+1, row-1
            lDown_left,lDown_down, rDown_right, rDown_down = col-1, row+1, col+1, row+1 
            while lUp_left >=0 and lUp_up >=0:
                b[lUp_up][lUp_left] = False
                lUp_left -= 1
                lUp_up -= 1
            while rUp_right <n and rUp_up >=0:
                b[rUp_up][rUp_right] = False
                rUp_right += 1
                rUp_up -= 1
            #print(b)
            #print("up")
            while lDown_left >=0 and lDown_down <n:
                b[lDown_down][lDown_left]=False
                lDown_left -= 1
                lDown_down += 1
            while rDown_right <n and rDown_down <n:
                b[rDown_down][rDown_right]=False
                rDown_right += 1
                rDown_down += 1
            #print(b)
            #print("down")
            return b
        def backTracking(row,count,board):
            if count == n:
                self.res += 1
                return count
            for col in range(n):
                #print(board)
                #print(count)
                #print("row:")
                #print(row)
                if board[row][col] == True:
                    #board = 
                    #if row == n-1:
                        #count += 1
                    
                    if row < n:
                        backTracking(row+1,count+1,placeQueen(row,col,board))

        board=[]
        for i in range(n):
            board.append([])
            for j in range(n):
                board[i].append(True)
        backTracking(0,0,board)
        return self.res