class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        arr = []
        for i in nums:
            print(arr)
            if len(arr) < 3 and i not in arr:
                arr.append(i)
            elif i > arr[0] and i not in arr:
                arr[0]=i
            arr.sort()
        if len(arr)  <2:
            return arr[0]
        elif len(arr)  <3:
            return arr[1]
        else:
            return arr[0]