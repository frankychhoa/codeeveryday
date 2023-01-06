class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        visited={}
        for i in s1:
            visited[i] = 1 + visited.get(i,0)
        foruse = copy.copy(visited)
        l,r = 0,0
        count = 0
        while r < len(s2):
            print(s2[r])
            print(count)
            print(foruse)
            if max(foruse.values()) == 0:
                return True
            if s2[r] not in foruse:
                l = r
                r += 1
                foruse = copy.copy(visited)     
            elif foruse[s2[r]]<=0:
                while s2[l] != s2[r]:
                    if s2[l] in foruse:
                        foruse[s2[l]] += 1
                    l += 1
                foruse[s2[r]] -= 1
                r += 1
                #oruse[s2[r]] += 1
            elif foruse[s2[r]]>0:
                foruse[s2[r]] -= 1
                r += 1
        # for key,val in foruse.items():
        #     if val != 0:
        #         return False 
        if max(foruse.values()) == 0:
            return True
        return False