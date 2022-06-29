import bisect
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        def possible(midn):
            for house in houses:
                ind=bisect.bisect_left(heaters,house)
                if (ind-1>=0 and heaters[ind-1]+midn>=house) or (ind<len(heaters) and heaters[ind]-midn<=house):
                    continue
                else:
                    return False
            return True

        l,r=0,max(max(houses)-min(houses),max(heaters))
        while(l<=r):
            mid=(l+r)//2
            if possible(mid):r=mid-1
            else:l=mid+1
        return l

