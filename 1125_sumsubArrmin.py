class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        #arr.sort()
        queue=[]
        s=set()
        d={}
        for n,i in enumerate(arr):
            queue.append([i])
            s.add(tuple([i]))
            d[tuple([i])] = n+1
        
        count=0
        index = 0
        while queue:
            element = queue.pop(0)
            
            m=element[0]
            for i in range(index,len(arr)):
                #print(arr[i])
                if arr[i] < m:
                    m = arr[i]
                count += m
            index+=1
            
        count%=(10**9+7)
        return count