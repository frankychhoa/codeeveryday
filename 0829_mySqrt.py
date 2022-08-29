class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        for i in range(x+1):
            
            if (i*i == x):
                return i
            
            elif x > i*i and x < (i+1)*(i+1) :

                return i