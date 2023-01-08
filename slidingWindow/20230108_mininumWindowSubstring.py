class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d ={}
        for i in t:
            d[i] = 1 + d.get(i,0)
        visited={}
        have, need= 0, len(d)
        res=""
        l=0
        for r in range(len(s)):
            #print(visited)
            visited[s[r]] = 1 + visited.get(s[r],0)
                
            if s[r] in d and visited[s[r]] == d[s[r]]:
                have += 1
            while have == need:
                #print(s[l:r+1])
                if not res:
                    res = s[l:r+1]
                elif len(s[l:r+1]) < len(res):
                    res = s[l:r+1]
                visited[s[l]] -= 1
                if s[l] in d and visited[s[l]] < d[s[l]]:
                    have -= 1
                l+=1
                
        return res