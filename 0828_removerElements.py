class Solution:
    def removeElement(self, nums, val: int) -> int:
        k = 0
        for i,j in enumerate(nums):
            if (j != val):
                nums[k] = j
                k+=1
        print(nums[:k])
        return k