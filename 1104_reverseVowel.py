class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=['a','e','i','o','u','A','E','I','O','U']
        sArr=[]
        for i in s:
            sArr.append(i)
        ptr1=0
        ptr2=len(s)-1
        while ptr1 < ptr2:
            while ptr2 >= 0 and s[ptr2] not in vowel  :
                ptr2 -= 1
            while ptr1 < len(s) and s[ptr1] not in vowel:
                ptr1 += 1
            print(ptr1)
            print(ptr2)
            if ptr1 < ptr2:
                temp = sArr[ptr1]
                sArr[ptr1] = sArr[ptr2]
                sArr[ptr2] = temp
                ptr1 += 1
                ptr2 -= 1
        res=""
        for i in sArr:
            res += i
        return res