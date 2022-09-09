class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        s = 0
        while n :
            print(2**count)
            if 2**count == n:
                return True
            elif 2**count > n:
                break
            count += 1
        return False