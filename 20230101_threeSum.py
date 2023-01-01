class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)): 
        #positive => result should be negative 
            if nums[i]-0 >=0:
                l,r = 0,len(nums)-1
                while l<r:
                    if nums[i]+nums[l]+nums[r] == 0 and i != r and i != l:
                        res.append([nums[i],nums[l],nums[r]])
                        l += 1
                    elif nums[l]+nums[r] > 0:
                        break
                    elif (nums[l]+nums[r]) >= (0-nums[i]):
                        r -= 1
                    else:
                        l += 1
            #nigative => result should be positive
            elif nums[i]-0 < 0 :
                l,r = 0,len(nums)-1
                while l<r:
                    if nums[i]+nums[l]+nums[r] == 0 and i != r and i != l:
                        res.append([nums[i],nums[l],nums[r]])
                        l += 1
                    elif nums[l]+nums[r] < 0:
                        break
                    elif (nums[l]+nums[r]) <= (0-nums[i]):
                        r += 1
                    else:
                        l -= 1
        return res