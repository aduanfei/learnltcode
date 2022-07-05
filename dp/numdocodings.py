class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            if s[0] == "0":
                return 0
            return 1
        if not s[0] == "0" and not s[1] == "0":
            if int(s[0:2]) <= 26:
                n1 = 1
                n2 = 2
            else:
                n1 = 1
                n2 = 1
        else:
            if s[0] == "0":
                n1 = 0
                n2 = 0
            else:
                n1 = 1
                if int(s[0:2]) <= 26:
                    n2 = 1
                else:
                    n2 = 0

        for i in range(2, len(s)):
            n3 = 0
            if not s[i - 1] == "0":
                if int(s[i - 1:i + 1]) <= 26:
                    n3 = 1
            if s[i] == "0":
                temp = n1 * n3
            else:
                temp = n1 * n3 + n2
            n1 = n2
            n2 = temp
        return n2