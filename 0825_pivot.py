class Solution:
    def pivotIndex(self, nums) -> int:
        total = sum(nums)
        count = 0
        for i in range(len(nums)):
            
            if count == total-count-nums[i]:
                return i
            count += nums[i]
        return -1