class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        sum1 = sum(stones)
        target = sum1 // 2
        dp = [0] * (target + 1)
        for i in range(len(stones)):
            #for t in range(stones[i], target + 1): t遍历必须逆序，保证dp是在i-1轮的情况
            for t in range(target,stones[i]-1,-1):
                dp[t] = max(dp[t - stones[i]] + stones[i], dp[t])
        print(dp[target])
        return sum1 - 2 * dp[target]

s=Solution()
s.lastStoneWeightII([31,26,33,21,40])