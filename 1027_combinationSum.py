class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ##BFS
        res=[]
        queue = []
        for i in candidates:
            queue.append([i])
        while queue:
            s = queue.pop(0)
            if sum(s) == target and s not in res:
                res.append(s)
            elif sum(s) < target:
                index = candidates.index(s[-1])
                for i in range(index,len(candidates)):
                    queue.append(s+[candidates[i]])
        return res