class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i,j in enumerate(nums):
            if j==target and len(res)<2:
                res.append(i)
            elif j == target:
                res.pop()
                res.append(i)
        if len(res) ==1 :
            return res+res
        elif len(res) > 1:
            return res
        return [-1,-1]