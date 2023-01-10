class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        #cur = max(piles)
        l,r = 0, max(piles)
        #cur = (l+r)//2
        m = 0
        while True:
            count = 0
            cur = (l+r)//2
            #print(cur)
            if cur == 0:
                break
            for i in piles:
                if i <= cur:
                    count += 1
                elif i%cur != 0:
                    count += (i//cur+1)
                else:
                    count += (i//cur)
            #print(count)
            if count <= h:
                m = count
                res = cur
                r = cur
            else:
                l = cur
            if (l+r)//2 == cur:
                break
        return res