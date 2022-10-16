class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited={}
        for i,j in enumerate(grid):
            for x,y in enumerate(j):
                self.visited[(i,x)]=False
        print(self.visited)
        def dfs(self,p):
            if self.visited[(p[0],p[1])]==False and  grid[p[0]][p[1]] == "1":
                self.visited[(p[0],p[1])]=True
                if p[0] < len(grid)-1:
                    dfs(self,(p[0]+1,p[1]))
                if p[1] < len(grid[0])-1:
                    dfs(self,(p[0],p[1]+1))
                if p[0] > 0:
                    dfs(self,(p[0]-1,p[1]))
                if p[1] > 0:
                    dfs(self,(p[0],p[1]-1))
        count=0
        for i,j in enumerate(grid):
            for x,y in enumerate(j):
                if self.visited[(i,x)]==False and grid[i][x]=="1":
                    count+=1
                    dfs(self,(i,x))
        return count