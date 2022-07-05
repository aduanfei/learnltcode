class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        self.dp = [[-1] * len(prices) for _ in range(len(prices))]
        self.prices = prices

        return self.maxp(0, len(prices) - 1)

    def maxp(self, n1, n2):
        if n2 <= n1:
            return 0
        if not self.dp[n1][n2] == -1:
            return self.dp[n1][n2]
        res = self.prices[n2] - self.prices[n1]
        if n2 - n1 == 1:
            return max(res, 0)
        for i in range(n1 - 1, n2):

            temp = self.maxp(n1, i) + self.maxp(i + 2, n2)
            if temp > res:
                res = temp
        self.dp[n1][n2] = max(res, 0)
        return max(res, 0)

#设置两个数组进行dp
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        self.dp = [[-1] * len(prices) for _ in range(len(prices))]
        self.prices = prices

        return self.maxp(0, len(prices) - 1)

    def maxp(self, n1, n2):
        if n2 <= n1:
            return 0
        if not self.dp[n1][n2] == -1:
            return self.dp[n1][n2]
        res = self.prices[n2] - self.prices[n1]
        if n2 - n1 == 1:
            return max(res, 0)
        for i in range(n1 - 1, n2):

            temp = self.maxp(n1, i) + self.maxp(i + 2, n2)
            if temp > res:
                res = temp
        self.dp[n1][n2] = max(res, 0)
        return max(res, 0)