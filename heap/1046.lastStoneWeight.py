import collections
import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones=[-x for x in stones]
        heapq.heapify(stones)
        while(stones):
            largest=-heapq.heappop(stones)
            if not stones:
                return largest
            smallst=-heapq.heappop(stones)
            remainst=largest-smallst
            if remainst:
                heapq.heappush(stones,-remainst)
        return 0

stones=[2,7,4,1,8,1]
s=Solution()
print(s.lastStoneWeight(stones))