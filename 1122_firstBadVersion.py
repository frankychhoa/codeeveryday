# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 1,n
        if isBadVersion(l) == True:
            return l 
        while l<=r:
            m = (l+r)//2
            if isBadVersion(m)==False:
                if isBadVersion(m+1) == True or m+1 == n:
                    return m+1
                else:
                    l=m
            else:
                r=m