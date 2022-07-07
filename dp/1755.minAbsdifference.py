#获得所有可能子集和分两个数组后用双指针

class Solution(object):
    def minAbsDifference(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """

        def combinesum(A):
            n = len(A)
            dp = [0] * ((1 << n))
            for i in range(n):
                for j in range((1 << i)):
                    dp[(1 << i) + j] = dp[j] + A[i]
                    #print(dp)
            return dp

        B = len(nums)
        n1 = combinesum(nums[:B // 2])
        n2 = combinesum(nums[B // 2:])

        n1.sort()
        n2.sort()
        #print(n1, "\n", n2)
        l = 0
        k = len(n2) - 1
        ans = float("inf")
        while (l < len(n1) and k >= 0):
            dif = n2[k] + n1[l]
            ans = min(ans, abs(dif-goal))
            if dif < goal:
                l += 1
            else:
                k -= 1
        return ans
