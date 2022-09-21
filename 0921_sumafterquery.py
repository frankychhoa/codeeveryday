class Solution:
    def sumEvenAfterQueries(self, nums, queries):
        count = 0
        for i in nums:
            if i%2 == 0:
                count += i
        result = []
        for i in queries:
            if nums[i[1]]%2 == 0:
                count -= nums[i[1]]
            nums[i[1]] += i[0]
            if nums[i[1]]%2 == 0:
                count += nums[i[1]]
            result.append(count)
        return result