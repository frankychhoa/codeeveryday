class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 0
        while p2 < len(nums) and p1 < len(nums) :
            if nums[p2] == 0:
                p2 += 1
            elif nums[p2] != 0 and p2 > p1:
                nums[p1] = nums[p2]
                nums[p2] = 0
                p1+=1
                p2+=1
            else:
                
                p2 += 1
                
            if nums[p1] != 0:
                p1 += 1
            
            
            
            
        return nums