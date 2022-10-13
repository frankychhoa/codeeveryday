class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def bf(lock):
            res=[]
            for i in range(len(lock)):
                num1=str((int(lock[i])+1)%10)
                res.append(lock[:i]+num1+lock[i+1:])
                num2=str((int(lock[i])-1+10)%10)
                res.append(lock[:i]+num2+lock[i+1:])
            return res
        if "0000" in deadends:
            return -1
        q=[]
        q.append(["0000",0])
        visited=set(deadends)
        while q:
            #print(visited)
            item=q.pop(0)
            lock, step=item[0],item[1]
            if lock==target:
                return step
            for i in bf(lock):
                if i not in visited:
                    q.append([i,step+1])
                    visited.add(i)
        return -1