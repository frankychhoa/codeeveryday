class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res=""
        count = 0
        while count < len(s):
            rev=""
            try:
                for i in range(k):
                    rev = s[count]+rev
                    count += 1 
                res += rev
            except:
                res += rev
                break
            try:
                for i in range(k):
                    res += s[count]
                    count += 1
            except:
                break
        return res