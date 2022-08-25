class Solution:
    def dominantIndex(self, nums) -> int:
        src = copy.copy(nums)
        src.sort()
        print(src)
        print(nums)
        if (src[-1] >= src[-2]*2):
            return nums.index(src[-1])
        return -1