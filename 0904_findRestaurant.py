class Solution:
    def findRestaurant(self, list1, list2) -> List[str]:
        m = {}
        for i,j in enumerate(list1):
            m[j] = i
        index_2 = []
        least = 2001
        
        for i,j in enumerate(list2):
            if j in m:
                if i+m[j] < least:
                    least = i+m[j]
                    index_2 = [i]
                elif i+m[j] == least:
                    index_2.append(i)
        result = []
        for i in index_2:
            result.append(list2[i])
        return result