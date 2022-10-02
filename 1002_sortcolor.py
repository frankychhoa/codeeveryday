class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i] += 1
        res=[]
        for i in range(3):
            if i in d:
                for j in range(d[i]):
                    res.append(i)
        for i in range(len(nums)):
            nums[i] = res[i]