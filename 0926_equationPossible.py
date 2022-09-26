#0926 not complete
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        for i in equations:
            x = i[0]
            y = i[3]
            f = i[1:3]
            d = []
            if x not in d:
                d[x] = Param(x)
            if y not in d:
                d[y] = Param(y)
            if f == "==":
                if d[y].alphabet in d[x].inequal:
                    return False
                else:
                    d[x].addEqual(d[y])
                    d[y].addEqual(d[x])
            elif f == "!=":
                if d[y].alphabet in d[x].equal:
                    return False
                else:
                    d[x].addInEqual(d[y])
                    d[y].addInEqual(d[x])
        return True


class Param:
    def __init__(self,x) -> None:
        self.alphabet=x
        self.equal=[]
        self.inequal=[]
    def addEqual(self,x):
        self.equal.append(x)
    def addInEqual(self,x):
        self.inequal.append(x)