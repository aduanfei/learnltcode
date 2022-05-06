import heapq
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        l=[1]
        heapq.heapify(l)
        count=1
        pre=1
        while(count<n):
            num=heapq.heappop(l)
            for p in primes:
                heapq.heappush(l,p*num)
            if not pre==num:
                count+=1
                pre=num
        return pre