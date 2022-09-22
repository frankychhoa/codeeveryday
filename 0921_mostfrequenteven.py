class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i%2 == 0:
                if i not in d:
                    d[i] = 1
                else:
                    d[i] += 1
        m = 0
        result = -1
        for i in d:
            if d[i] > m:
                result = i
                m=d[i]
            elif d[i] == m and i<result:
                result = i
        return result