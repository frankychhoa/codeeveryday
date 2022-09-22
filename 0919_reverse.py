class Solution:
    def reverse(self, x: int) -> int:
        
        
        count = 0
        power = 0
        i = abs(x)
        while i/(10**power) >= 1:
            power += 1
        power -= 1
        while i >=1:
            count += (i%10)*(10**power)
            power -= 1
            i //= 10
        if x < 0 and count > 0:
            count*=(-1)
        if count< -(2**31) or count > (2**31-1):
            return 0
        return count