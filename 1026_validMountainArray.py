class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_index=arr.index(max(arr))
        l,r = max_index-1, max_index+1
        left,right = arr[max_index], arr[max_index]
        if l < 0 or r == len(arr):
            return False
        while l >=0 or r < len(arr):

            if l>=0 and arr[l] >= left:
                return False
            if r < len(arr) and arr[r] >= right:
                return False
            if l >=0:
                left=arr[l]
            if r <len(arr):
                right=arr[r]
            l -= 1
            r += 1
        return True