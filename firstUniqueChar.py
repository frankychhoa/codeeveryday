class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}
        index = 0
        for i in s:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        for i,j in enumerate(s):
            if m[j] == 1:
                return i
        return -1