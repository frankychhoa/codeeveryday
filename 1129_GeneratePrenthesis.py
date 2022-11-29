class Solution:
    def __init__(self):
        self.res=[]
    def generateParenthesis(self, n: int) -> List[str]:
        def fun(s,close,ope):
            if close == n and ope == n:
                self.res.append(s)
            elif close <= ope and ope <= n:
                fun(s+"(",close,ope+1)
                fun(s+")",close+1,ope)
        fun("(",0,1)
        return self.res