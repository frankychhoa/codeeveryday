class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k -= len(nums)
        origin = copy.deepcopy(nums)
        for i in range(len(nums)):
            #origin[i] = nums[i]
            if i <k:
                
                nums[i] = origin[len(nums)-k+i]
            else:
                nums[i] = origin[i-k]