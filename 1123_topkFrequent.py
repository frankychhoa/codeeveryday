class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        res=[]
        for i in nums:
            if i not in d:
                d[i]=1
                res.append(i)
            else:
                d[i]+=1
        res=[]
        print(d)
        for i in d:
            
            if len(res) == 0:
                res.append(i)
            else:
                if d[i] <= d[res[-1]]:
                    res.append(i)
                elif d[i] > d[res[0]]:
                    res.insert(0,i)
                else:
                    for r in range(len(res)-1):
                        if r == 0 and d[i] > d[res[r]]:
                            res.insert(r,i)
                            break
                        elif d[i] <= d[res[r]] and d[i] > d[res[r+1]]:
                            
                            res.insert(r+1,i)
                            break
            #print(res)
        return res[:k]