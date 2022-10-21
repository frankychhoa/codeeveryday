class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for i,j in enumerate(nums):
            if j not in d:
                d[j]=i
            elif i-d[j] <= k:
                return True
            else:
                d[j]=i
        return False