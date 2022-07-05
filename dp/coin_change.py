class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        dp = [-1] * (amount + 1)
        for am in range(1, amount + 1):
            for c in coins:
                if am == c:
                    dp[am] = 1

                if am - c > 0 and not dp[am - c] == -1:
                    if dp[am] == -1 or dp[am - c] + 1 < dp[am]:
                        dp[am] = dp[am - c] + 1

        return dp[amount]
