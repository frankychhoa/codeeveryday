class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        def merge(left,right):
            res=[]
            while len(left) !=0 or len(right)!=0:
                if len(left) == 0:
                    res += right
                    right=[]
                elif len(right) ==0:
                    res += left
                    left=[]
                elif left[0] <= right[0]:
                    res.append(left.pop(0))
                elif left[0] > right[0]:
                    res.append(right.pop(0))
            return res
        
        def recur(arr):
            if len(arr) <= 1:
                return arr
            l,r=[],[]
            l,r = arr[:len(arr)//2], arr[len(arr)//2:]

            left = recur(l)
            right = recur(r)

            return merge(left,right)
        ans = recur(nums)
        
        return ans