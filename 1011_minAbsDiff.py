class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        d={}
        m=arr[1]-arr[0]
        for i in range(len(arr)-1):
            diff=abs(arr[i+1]-arr[i])
            if diff not in d:
                d[diff]=[[arr[i],arr[i+1]]]
            else:
                d[diff].append([arr[i],arr[i+1]])
            if  diff < m:
                m = diff
        return d[m]