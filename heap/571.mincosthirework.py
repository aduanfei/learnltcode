import heapq

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """
        eff=[(b/a,a,b)for a,b in zip(quality,wage)]
        eff.sort()
        res=float('inf')
        for i in range(k-1,len(eff)):
            h=[]
            total=0
            num=k
            qw=eff[i][0]
            for j in range(i+1):
                heapq.heappush(h,eff[j][1]*qw)
            while(num>0):
                num-=1
                total+=heapq.heappop(h)
            res=min(res,total)
        return res




quality = [3,1,10,10,1]
wage = [4,8,2,2,7]
k = 3
s=Solution()
print(s.mincostToHireWorkers(quality,wage,k))