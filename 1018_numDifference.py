class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            d[i]=True
        
        res=[]
        for i in range(1,len(nums)+1):
            try:
                if d[i]==True:
                    continue
            except:
                res.append(i)
        return res