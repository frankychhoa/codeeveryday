class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for i in magazine:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in ransomNote:
            if i in d:
                d[i] -= 1
                if d[i] < 0:
                    return False
            else:
                return False
        return True