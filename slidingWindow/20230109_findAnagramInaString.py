class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        d={}
        for i in p:
            d[i] = 1 + d.get(i,0)
        visited=copy.copy(d)
        for r in range(len(p)):
            if s[r] in visited:
                visited[s[r]] -= 1
        
        l,r = 0,len(p)-1
        res=[]
        #if max(visited.values()) == 0:
            #res.append(l)
        
        while r < len(s):
            if max(visited.values()) == 0:
                res.append(l)
            if s[l] in visited:
                visited[s[l]] += 1
            l += 1
            
            r += 1
            try:
                if s[r] in visited:
                    visited[s[r]] -= 1
            except:
                pass
        return res