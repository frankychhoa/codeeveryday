class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(len(queries)):
            res.append(0)
        for i in range(len(queries)):
            total=0
            count=0
            for j in nums:
                if total > queries[i]:
                    count-=1
                    break
                else:
                    total += j
                    count += 1
            if count == len(nums):
                if total > queries[i]:
                    res[i] = count-1
                else:
                    res[i] = count
            else:
                res[i] = count
        return res