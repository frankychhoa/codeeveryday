class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        res=[]
        d={"2":"abc",
           "3":"def",
           "4":"ghi",
           "5":"jkl",
           "6":"mno",
           "7":"pqrs",
           "8":"tuv",
           "9":"wxyz"
          }
        def add(s,q):
            #print(q)
            if len(q)==0:
                res.append(s)
            else:
                element = q[0]
                for i in d[element]:
                    #s += i
                    add(s+i,q[1:])
        queue=[]
        for i in range(1,len(digits)):
            queue.append(digits[i])
        for i in d[digits[0]]:
            add(i,queue)
        return res