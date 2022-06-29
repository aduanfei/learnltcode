class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        if not s:
            return ""

        dps=[[-1 for _ in range(len(s))] for _ in range(len(s))]
        for j in range(0, len(s)):
            for i in range(j, -1, -1):
                if i==j:
                    dps[i][j]=s[i]
                elif dps[i][j] == -1:
                    if s[i] == s[j]:
                        if i + 1 <= j - 1:
                            if not dps[i + 1][j - 1] == "":
                                dps[i][j] = s[i] + dps[i + 1][j - 1] + s[j]
                            else:
                                dps[i][j] = ""
                        else:
                            dps[i][j] = s[i] + s[j]
                        if len(dps[i][j]) > len(ans):
                            ans = dps[i][j]
                    else:
                        dps[i][j] = ""
        return ans

s=Solution()
print(s.longestPalindrome("babad"))