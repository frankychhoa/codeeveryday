class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s:
            return 0
        g.sort()
        s.sort()
        count = 0
        while len(g) > 0 and len(s) > 0:
            if g[0] <= s[0]:
                count += 1
                g.pop(0)
            s.pop(0)
            
                
        return count