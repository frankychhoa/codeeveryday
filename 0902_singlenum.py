class Solution:
    def singleNumber(self, nums) -> int:
        
        nums.sort()
        print(nums)
        while len(nums) > 0:
            if (len(nums)==1):
                return nums[0]
            elif nums[0] == nums[1]:
                nums.pop(0)
                nums.pop(0)
            else:
                return nums[0]