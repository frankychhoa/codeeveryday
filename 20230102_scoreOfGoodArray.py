class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        m=nums[k]
        l,r=k,k
        maximum = m*((r-l)+1)
        while l>0 or r<=len(nums)-1:
            if l == 0:
                r +=1
            elif r == len(nums)-1:
                l -= 1
            elif nums[l-1] > nums[r+1]:
                l-=1
            else:
                r += 1
            try:
                m = min(m,min(nums[l],nums[r]))
                tem = m*(r-l+1)
                if tem > maximum:
                    maximum = tem
            except:
                pass

        return maximum