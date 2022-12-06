class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for n,i in enumerate(list(string.ascii_lowercase)):
            d[i] = n
        res={}
        for i in strs:
            key=[0 for i in range(26)]
            for s in i:
                key[d[s]] += 1
            if tuple(key) not in res:
                res[tuple(key)] = [i]
            else:
                res[tuple(key)] += [i]
        answer=[]
        for i in res:
            answer.append(res[i])
        return answer