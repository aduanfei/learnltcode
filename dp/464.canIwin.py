#先解出递归然后状态压缩dp

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if desiredTotal < maxChoosableInteger:
            return True
        if sum(range(maxChoosableInteger + 1)) < desiredTotal:
            return False

        def canwin(picked, cum):
            if cum >= desiredTotal:
                return False
            if picked == (1 << (maxChoosableInteger + 1)) - 1:
                return False
            for i in range(1, maxChoosableInteger + 1):
                if picked & 1 << i == 0:
                    if not canwin(picked | 1 << i, cum + i):
                        return True

            return False

        return canwin(0, 0)


class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if desiredTotal < maxChoosableInteger:
            return True
        if sum(range(maxChoosableInteger + 1)) < desiredTotal:
            return False

        def canwin(picked, cum):
            if cum >= desiredTotal:
                return False
            for i in range(1, maxChoosableInteger + 1):
                if picked & 1 << i == 0:
                    if not canwin(picked | 1 << i, cum + i):
                        return True

            return False

        return canwin(0, 0)


s=Solution()
print(s.canIWin(10,11))