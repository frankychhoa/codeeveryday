# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        r = n
        l = 1
        x = n
        while guess(x) != 0:
            if guess(x) == -1:
                r=x
                x = (r+l)//2
            elif guess(x) == 1:
                l=x
                x=(r+l)//2
        return x