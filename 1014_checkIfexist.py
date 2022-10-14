class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d={}
        for i,j in enumerate(arr):
            d[j]=i
        for i,j in enumerate(arr):
            try:
                if d[j/2]!=i:
                    return True

            except:
                continue
        return False