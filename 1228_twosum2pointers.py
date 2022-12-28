class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1, ptr2 = 0, len(numbers)-1
        while ptr1 < ptr2:
            if numbers[ptr1] + numbers[ptr2] == target:
                return [ptr1+1,ptr2+1]
            elif numbers[ptr1] + numbers[ptr2] < target:
                ptr1 += 1
            elif numbers[ptr1] + numbers[ptr2] > target:
                ptr2 -= 1