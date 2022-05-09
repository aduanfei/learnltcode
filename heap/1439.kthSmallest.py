#指针数据要转换为元组，排除重复项

import heapq
import copy
class Solution(object):
    def kthSmallest(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: int
        """
        h = []
        sum1 = sum([vec[0] for vec in mat])
        m = len(mat)
        seen=set()
        h = [(sum1, [0] * m)]
        count = 0
        seen.add(tuple([0]*m))
        while (count < k and h):
            cur = heapq.heappop(h)
            count += 1
            for i in range(m):
                ind = cur[1][i] + 1
                if ind < len(mat[0]):
                    sum2 = cur[0] + mat[i][ind] - mat[i][ind - 1]
                    m2 = copy.deepcopy(cur[1])
                    m2[i] = ind
                    if not tuple(m2) in seen:
                        heapq.heappush(h, (sum2, m2))
                        seen.add(tuple(m2))
        return cur[0]

s=Solution()
mat=[[1,3,11],[2,4,6]]
k=9
print(s.kthSmallest(mat,k))