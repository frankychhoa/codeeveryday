class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ref=0
        if a>b:
            ref=b
        else:
            ref=a
        count=0
        for i in range(ref):

            if a%(i+1)==0 and b%(i+1)==0:
                count += 1
        return count