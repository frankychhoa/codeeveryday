class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        try:
            res = nums.index(target)
        except:
            res = -1
        return res