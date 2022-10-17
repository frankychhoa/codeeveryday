class Solution:
    def numSquares(self, n: int) -> int:
        m = int(math.sqrt(n))
        queue = []
        visited={}
        for i in range(1,m+1):
            queue.append([i**2,1,i])
            visited[i**2]=True
        while queue:
            #print(queue)
            element = queue.pop(0)
            if element[0]==n:
                return element[1]
            for i in range(element[2],m+1):
                try:
                    if visited[element[0]+i**2] == True:
                        continue
                #if element[0]+i**2 not in visited:
                except:
                    visited[element[0]+i**2]=True
                    queue.append([element[0]+i**2,element[1]+1,i])