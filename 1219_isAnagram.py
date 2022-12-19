class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1={}
        d2={}
        for i in s:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
        for i in t:
            if i not in d2:
                d2[i] = 1
            else:
                d2[i] += 1
        for k in d1:
            try:
                if d1[k] != d2[k]:
                    return False
            except:
                return False
        return True