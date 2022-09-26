class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        d = {}
        count=0
        for i in candyType:
            if i not in d:
                count += 1
                d[i] = True
        if count >= len(candyType)/2:
            count = int(len(candyType)/2)
        return count