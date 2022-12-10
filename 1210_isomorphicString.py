class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sq = list(string.ascii_lowercase)
        tq = list(string.ascii_lowercase)
        sd, td = {},{}
        for n,i in enumerate(s):
            if i not in sd:
                sd[i]=[n]
            else:
                sd[i] += [n]
        for n,i in enumerate(t):
            if i not in td:
                td[i]=[n]
            else:
                td[i] += [n]

        for i in range(len(s)):
            if sd[s[i]] != td[t[i]]:
                return False
        return True