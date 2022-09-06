class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        m = {}
        for i,j in enumerate(nums):
            if j not in m:
                m[j] = i
            elif i - m[j]  <= k:
                return True
            else:
                m[j] = i
        return False