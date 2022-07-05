class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for gap in range(0, n):
            for i in range(0, n - gap):
                if dp[i][i + gap] == 0:
                    if gap == 0:
                        dp[i][i] = piles[i]
                    else:
                        dp[i][i + gap] = max(piles[i] - dp[i + 1][i + gap], piles[i + gap] - dp[i][i + gap - 1])
        return dp[0][n - 1] > 0
