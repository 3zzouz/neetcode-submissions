class Solution:
    def isThisRateEnough(self,piles:List[int],h:int , k:int) -> tuple[bool,int] :
        nbhour = 0
        for e in piles:
            nbhour += math.ceil(e/k)
        return nbhour <= h , nbhour
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = piles[0]
        for e in piles :
            m = max(m,e)
        res = m
        l = 1
        r = m
        while l < r :
            mil = int((r+l)/2)
            isok,_ = self.isThisRateEnough(piles,h,mil)
            if isok:
                r = mil
                res = min(res,mil)
            else :
                l = mil+1
        return res