class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def duplicate(s,nextStr):
            if len(s) > len(set(s)):
                return False
            for i in nextStr:
                if i in set(s):
                    return False
            return True
        def dup(s):
            if len(s) > len(set(s)):
                return False
            return True
        def backtrack(s,i):
            print(s)
            if i == len(arr):
                return len(s)
            res=0
            nextStr=arr[i]
            if duplicate(s,nextStr)==True:
                origin=s
                if dup(nextStr) == True:
                    s += nextStr
                res=backtrack(s,i+1)
                s=origin
                #s = s[:len(s)-len(nextStr)]
            return max(res,backtrack(s,i+1))
        return backtrack("",0)