class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i,j in enumerate(string.ascii_lowercase):
            d[j]=i
        m={}
        for i in strs:
            buckets = [0] * 26
            for j in i:
                buckets[d[j]]+=1
            if tuple(buckets) not in m:
                m[tuple(buckets)]=[i]
            else:
                m[tuple(buckets)]+=[i]
        res=[]
        for i in m:
            res.append(m[i])
        return res