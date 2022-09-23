class Solution:
    def concatenatedBinary(self, n: int) -> int:
        def toBin(num):
            b=""
            while num >=1:
                if num%2 !=0:
                    b = "1"+b
                else:
                    b = "0"+b
                num //= 2
            return b
        modulo = 10**9+7
        power=0
        result=0
        s=""
        for i in range(n):
            s+=toBin(i+1)
            #s+=bin(i+1)[2:]
        index=len(s)-1
        #print(s)
        for i in range(len(s)):
            result+=2**power*int(s[index])
            power+=1
            index-=1
        #int(s, 2)
        return result%modulo