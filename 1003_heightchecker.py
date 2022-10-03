class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        origin = copy.copy(heights)
        #bubble sort
        has_swapped=True
        while has_swapped:
            has_swapped=False
            for i in range(len(heights)-1):
                if heights[i] > heights[i+1]:
                    temp=heights[i]
                    heights[i]=heights[i+1]
                    heights[i+1]=temp
                    has_swapped=True
        print(heights)
        count=0
        for i in range(len(heights)):
            if origin[i] != heights[i]:
                count+=1
        return count