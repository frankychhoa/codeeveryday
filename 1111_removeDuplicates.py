class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1=0
        ptr2=0
        while ptr2 < len(nums):
            if nums[ptr1] == nums[ptr2]:
                ptr2+=1
            elif ptr2-ptr1 > 1:
                nums[ptr1+1] = nums[ptr2]
                ptr1+=1
                ptr2+=1
            else:
                
                ptr1+=1
                ptr2+=1
        for i in range(ptr1+1,ptr2):
            nums.pop()