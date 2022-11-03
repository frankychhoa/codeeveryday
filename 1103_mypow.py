class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n==0:
            return 1
        elif n>0 and n%2 == 1:
            return x * self.myPow(x,n-1)
        elif n>0 and n%2 == 0:
            return self.myPow(x*x, n/2)
        else:
            return self.myPow(1/x,-n)