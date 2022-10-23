class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res=[]
        s=set()
        miss=0
        duplicate=0
        nums.sort()
        for i,j in enumerate(nums):
            if j not in s:
                s.add(j)
            else:
                duplicate=j
        for i in range(len(nums)):
            if i+1 not in s:
                miss=i+1
        return [duplicate,miss]