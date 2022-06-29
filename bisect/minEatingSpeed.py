class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def possible(piles,h,midn):
            res=0
            for p in piles:
                res+= (p + midn - 1) // mid
            if res<=h:
                return 1
            else:
                return 0
        if not piles or max(piles)==0:
            return 0
        l,r=1,max(piles)
        while(l<=r):
            mid=(l+r)//2
            if possible(piles,h,mid): r=mid-1
            else: l=mid+1
        return l