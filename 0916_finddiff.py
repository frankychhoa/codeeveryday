class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sd = {}
        td = {}
        i = 0
        while i < len(s) or i <len(t):
            if i < len(s):
                if s[i] in sd:
                    sd[s[i]] += 1
                else:
                    sd[s[i]] = 1
            if i < len(t):
                if t[i] in td:
                    td[t[i]] += 1
                else:
                    td[t[i]] = 1
            i +=1
        for i in td:
            if i not in sd:
                return i
            elif td[i] > sd[i]:
                return i