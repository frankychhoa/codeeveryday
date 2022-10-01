import string
class Solution:
    def __init__(self) -> None:
        self.ref={}

        for i,j in enumerate(list(string.ascii_uppercase)):
            self.ref[str(i+1)] = j
    def numDecodings(self, s: str) -> int:
        if len(s) == 1 and s != "0":
            return 1
        print(s)
        m={}
        self.dfs(m,0,s,s[0])
        print(m)
        if len(s) > 2:
            self.dfs(m,1,s,s[:2])
        if not m:
            return 0
        
        count=m[0]
        if s[0:2] in self.ref:
            if len(s) == 2:
                count+=1
            elif 1 in m:
                count +=m[1]
        return count
    
    def dfs(self,m,index,s,next):
        print(next)
        if next not in self.ref:
            return 0
        if index in m:
            return m[index]
        if index == len(s)-1:
            m[index] = 1
            if next in self.ref:
                return 1

        if index == len(s)-2:
            m[index] = self.dfs(m,index+1,s,s[index+1])
            return m[index] 
        else:
            n = ""+s[index+1]+s[index+2]
            m[index] = self.dfs(m,index+1,s,s[index+1]) + self.dfs(m,index+2,s,n)
            return m[index]