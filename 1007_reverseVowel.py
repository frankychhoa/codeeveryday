class Solution:
    def reverseVowels(self, s: str) -> str:
        d={}
        d[" "]=False
        #ASCII = ''.join(chr(x) for x in range(128))
        for i in list(string.printable):
            if i =='a' or i=='e' or i=='i' or i=='o' or i=='u' or i =='A' or i=='E' or i=='I' or i=='O' or i=='U':
                d[i]=True
            else:
                d[i]=False

        count=0
        index={}
        ref={}
        for i,j in enumerate(s):
            if d[j]==True:
                count+=1
                ref[count]=j
                index[i]=True
            else:
                index[i]=False
        res=""
        for i in range(len(s)):
            if index[i]==True:
                res+=ref[count]
                count-=1
            else:
                res+=s[i]
        
        return res