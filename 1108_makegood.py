class Solution:
    def makeGood(self, s: str) -> str:
        d = {}
        for i,j in enumerate(list(string.ascii_lowercase)):
            d[j] = list(string.ascii_uppercase)[i]
            d[list(string.ascii_uppercase)[i]]=j
        good=False
        s=list(s)
        while good == False:
            good = True
            #print(s)
            for i in range(len(s)-1):
                if d[s[i]] == s[i+1] :
                    try:
                        s=s[:i]+s[i+2:]
                    except:
                        s=s[:i]
                    good = False
                    break
        return "".join(s)