class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        start = False
        l = len(s)-1
        while l >= 0:
            if s[l] != " ":
                start = True
                count += 1
                l -= 1
            elif s[l] == " " and start == False:
                l -= 1
            elif s[l] == " " and start == True:
                break
        return count