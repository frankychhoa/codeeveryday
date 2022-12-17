class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        resLen=0
        for i in range(len(s)):
            l,r = i,i
            p=""
            while l>=0 and r<len(s) and s[l]==s[r]:
                p=s[l:r+1]
                l-=1
                r+=1
                
            if len(p) > resLen:
                res = p
                resLen = len(p)
            
            l,r = i,i+1
            p = ""
            while l>=0 and r<len(s) and s[l]==s[r]:
                p=s[l:r+1]
                l-=1
                r+=1

            if len(p) > resLen:
                res = p
                resLen = len(p)
        return res
