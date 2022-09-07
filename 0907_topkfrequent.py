class Solution:
    def topKFrequent(self, nums, k: int) :
        m = {}
        nums.sort()
        order = []
        for i,j in enumerate(nums):
            if j not in m:
                m[j] =1
                if len(order) == 0:
                    order.append(j)

                else:
                    for x,y in enumerate(order):
                        if m[nums[i-1]] >= m[y] and nums[i-1] != y:
                            order.insert(x,nums[i-1])
                            break
                    if nums[i-1] not in order:
                        order.append(nums[i-1])
            else:
                m[j] = m[j]+1
        for x,y in enumerate(order):
            if m[nums[-1]] >= m[y] and nums[-1] != y:
                order.insert(x,nums[-1])
                break
            if nums[i-1] not in order:
                order.append(nums[-1])
        result = order[:k]
        result.sort()
        return result