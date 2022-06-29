from sortedcontainers import SortedList
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        cur,ans=0,0
        pre=SortedList([0])
        for n in nums:
            cur+=n
            ans+=bisect.bisect_right(pre,cur-lower)-bisect.bisect_left(pre,cur-upper)
            pre.add(cur)
        return ans
