class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = []
        for i,q in enumerate(mat):
            for j,k in enumerate(q):
                if mat[i][j] == 0:
                    queue.append([(i,j),0])
                else:
                    queue.append([(i,j),0])
        countMap = dict()
        if len(queue)==1:
            return [[0]]
        while len(queue)!=0:
            element = queue.pop(0)
            print(element)
            i,j,count = element[0][0], element[0][1], element[1]
            neighbors = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
            con = True
            if mat[i][j] == 0:
                countMap[(i,j)] = 0
                con = False
            if con == True:
                for n in neighbors:
                    if n[0]>=0 and n[0]<len(mat) and n[1]>=0 and n[1]<len(mat[0]):
                        x,y = n[0],n[1]
                        if mat[x][y] == 0:
                            countMap[(i,j)] = count+1
                            con = False
            if con == True:
                plus=float('inf')
                f=False
                for n in neighbors:
                    x,y = n[0],n[1]
                    try:
                        b = countMap[(x,y)]
                        if countMap[(x,y)]==0:
                            b+=1
                        if  b < plus:
                            plus = countMap[(x,y)]
                        f = True
                    except:
                        continue
                if f == True:
                    countMap[(i,j)] = count+plus+1
                    con = False
            if con == True:
                queue.append([(i,j),count+1])
        res = mat
        
        for c in countMap:
            res[c[0]][c[1]] = countMap[c]
        return res