class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1=0
        ptr2=1
        while ptr2 < len(nums):
            if nums[ptr1] != nums[ptr2]:
                if ptr2 - ptr1 == 1:
                    ptr1 += 1
                    ptr2 += 1
                else:
                    nums[ptr1+1] = nums[ptr2]
                    ptr1 += 1
                    ptr2 += 1
            else:
                ptr2+=1
        for i in range(len(nums)-ptr1-1):
            nums.pop()