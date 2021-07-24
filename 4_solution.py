import math
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        res = [1]
        i2, i3, i5 = 0, 0, 0
        while (len(res) < n):
            print("here")
            m2 = res[i2] * 2
            m3 = res[i3] * 3
            m5 = res[i5] * 5
            mn = min(m2, min(m3, m5))
            if (mn == m2):
                m2 += 1
            if (mn == m3):
                m3 += 1
            if (mn == m5):
                m5 += 1
            res.append(mn)
        return res[-1]


if (__name__ == "__main__"):
    s = Solution()
#    assert(s.nthUglyNumber(7) == 8)
#    assert(s.nthUglyNumber(9) == 10)
    print(s.nthUglyNumber(41))
