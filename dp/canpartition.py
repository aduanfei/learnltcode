class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        nsu = sum(nums)
        if not nsu % 2 == 0:
            return False
        else:
            hals = nsu // 2
        dp = [[0] * (hals + 1) for _ in range(len(nums) + 1)]

        for i in range(1, len(nums) + 1):
            for ts in range(1, hals + 1):
                if ts == nums[i - 1]:
                    dp[i][ts] = 1
                elif dp[i][ts] == 0:
                    dp[i][ts] = dp[i - 1][ts]
                    if ts - nums[i - 1] >= 0:
                        dp[i][ts] = dp[i][ts] or dp[i - 1][ts - nums[i - 1]]

        return dp[len(nums)][hals] == 1