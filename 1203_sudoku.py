arr=[]
col_start=0
row_start=0
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
print(arr)
    