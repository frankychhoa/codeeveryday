class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1=0
        ptr2=1
        while ptr2 < len(nums):
            #print(nums)
            if nums[ptr1] == nums[ptr2]:
                ptr2+=1
            else:
                ptr1+=1
                nums[ptr1] = nums[ptr2]
                ptr2+=1
        return len(nums[:ptr1+1])