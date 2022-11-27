class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum=max(arr)
        maxIndex=arr.index(maximum)
        index=0
        while index < len(arr):
            if index < maxIndex:
                arr[index]=maximum
            elif index == maxIndex and index<len(arr)-1:
                maximum = max(arr[index+1:])
                maxIndex=index+1+arr[index+1:].index(maximum)
                print(arr[index+1:])
                print(maxIndex)
                arr[index]=maximum
            index+=1
        arr[-1]=-1
        return arr