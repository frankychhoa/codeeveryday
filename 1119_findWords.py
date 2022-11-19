class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1="qwertyuiop"
        s2="asdfghjkl"
        s3="zxcvbnm"
        d={}
        for i in s1:
            d[i] = 1
            d[i.upper()]=1
        for i in s2:
            d[i] = 2
            d[i.upper()]=2
        for i in s3:
            d[i] = 3
            d[i.upper()]=3
        
        res = []
        for i in words:
            row = d[i[0]]
            add = True
            for j in i:
                if d[j] != row:
                    add = False
            if add == True:
                res.append(i)
        return res