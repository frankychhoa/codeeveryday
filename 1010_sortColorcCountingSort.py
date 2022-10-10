class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ##practice counting sort
        count=[0,0,0]
        for i in nums:
            count[i]+=1
        ##startingindice
        indices=[0,0,0]
        start=0
        for i in range(len(count)):
            start+=count[i]
            indices[i]=start
        indices=[0]+indices[:-1]
        result=[]
        for i in range(len(nums)):
            result.append(0)
        for i in nums:
            print(indices)
            result[indices[i]] = i
            indices[i]+=1
        for i in range(len(nums)):
            nums[i] = result[i]