class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        d1, d2 = {},{}
        for i in nums1:
            for j in nums2:
                if i+j not in d1:
                    d1[i+j] = 1
                else:
                    d1[i+j] += 1
        for i in nums3:
            for j in nums4:
                if i+j not in d2:
                    d2[i+j] = 1
                else:
                    d2[i+j] += 1
        for i in d1:
            if -i in d2:
                count += d1[i]*d2[-i]
        return count