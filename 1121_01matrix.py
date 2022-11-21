class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue=[]
        visited=set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    queue.append((i,j))
                    visited.add((i,j))
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while queue:
            #print(queue)
            item = queue.pop(0)
            i,j=item[0],item[1]
            for d in direction:
                ni=i+d[0]
                nj=j+d[1]
                if ni >=0 and ni < len(mat) and nj >=0 and nj < len(mat[0]) and (ni,nj) not in visited:
                    mat[ni][nj]=mat[i][j]+1
                    visited.add((ni,nj))
                    queue.append((ni,nj))
        return mat