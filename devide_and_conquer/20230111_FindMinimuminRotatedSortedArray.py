class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] >= nums[0]:
            return nums[0]
        l,r = 0, len(nums)-1
        
        while True:
            cur = (l+r)//2
            if nums[cur] > nums[r]:
                l = cur
            else:
                r = cur
            if cur+1 <= len(nums)-1 and nums[cur] > nums[cur+1]:
                return nums[cur+1]
            elif cur -1 >=0 and nums[cur-1] > nums[cur]:
                return nums[cur]