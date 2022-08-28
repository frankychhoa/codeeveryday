class Solution:
    def twoSum(self, numbers, target: int):
        numMap = {}
        for i,j in enumerate(numbers):
            numMap[j] = i
        for i,j in enumerate(numbers):
            if (target-j) in numMap:
                return [i+1,numMap[target-j]+1]