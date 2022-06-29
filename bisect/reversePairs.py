from sortedcontainers import SortedList

import bisect
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        js = SortedList([])
        for i in range(len(nums)):
            n = nums[len(nums) - i - 1]

            res += bisect.bisect_left(js, n)
            js.add(2 * n)
        return res
