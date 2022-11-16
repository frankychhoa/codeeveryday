# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        x=0
        l,r = 1,n
        while r-l>1:  
            x = (l+r)//2
            if guess(x) == 0:
                return x
            elif guess(x) == -1:
                r = x
            else:
                l = x
        if guess(l) == 0:
            return l
        elif guess(l) == 0:
            return l
        return n