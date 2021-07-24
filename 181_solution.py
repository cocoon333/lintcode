"""
class Solution:
    @param a: An integer
    @param b: An integer
    @return: An integer
    def bitSwapRequired(self, a, b):
        s = bin(a^b)
        res = s.count('1')
        if ((a < 0 and b > 0) or (a > 0 and b < 0)):
            res += 32 - len(s) + 3
        return res
"""

class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: An integer
    """
    def bitSwapRequired(self, a, b):
        neg = False
        if ((a < 0 and b > 0) or (a > 0 and b < 0)):
            neg = True
            if (a < 0):
                a = -a
            else:
                b = -b
        s = bin(a^b)
        res = 0
        for i in range(len(s)):
            if s[i] == "1":
                res += 1
        if neg:
            res += 32 - len(s) + 2

        return res


if __name__ == "__main__":
    s = Solution()
    assert(s.bitSwapRequired(31, 14) == 2)
    assert(s.bitSwapRequired(1, 7) == 2)
    assert(s.bitSwapRequired(-1, 1) == 31)
    assert(s.bitSwapRequired(-64, 32) == 27)
    assert(s.bitSwapRequired(-2147483648, 11) == 4)
