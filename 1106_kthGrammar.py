##ref https://www.youtube.com/watch?v=L9ha9WUwTtc
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0 
        parent=self.kthGrammar(n-1,k//2+k%2)
        isOdd= (k%2 == 1)
        if parent == 1:
            if isOdd==True:
                return 1
            else:
                return 0
        else:
            if isOdd==True:
                return 0
            else:                                        
                return 1