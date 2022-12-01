class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels=set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        countFst,countSec=0,0
        for i in range(len(s)):
            if i < len(s)//2 and s[i] in vowels:
                countFst += 1
            elif i >= len(s)//2 and s[i] in vowels:
                countSec += 1
        if countFst == countSec:
             return True
        return False