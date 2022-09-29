class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        arr = [2,3,5]
        while n > 1:
            print(n)
            for i in arr:
                if n % i == 0:
                    n //= i
                    break
                elif n%i !=0 and i==5:
                    return False
        return True