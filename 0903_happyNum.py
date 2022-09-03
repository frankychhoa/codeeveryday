class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n not in s:
            s.add(n)
            count = 0
            while n:
                count += (n%10)**2
                n = n//10
            if count == 1:
                return True
            n = count
            
            
            
        return False