class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        p=0
        while n >= 4**p:
            if n == 4**p:
                return True
            p+=1
        return False