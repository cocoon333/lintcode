class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """
    def getNarcissisticNumbers(self, n):
        res = []
        if (n == 1):
            res.append(0)
        for i in range(10**(n-1), 10**n):
            if (self.isNarcissisticNumbers(i, n)):
                res.append(i)
        return res

    def isNarcissisticNumbers(self, j, n):
        digits = list(map(int, str(j)))
        res = 0
        for i in range(len(digits)):
            res += digits[i] ** n
        return (res == j)

if (__name__ == "__main__"):
    s = Solution()
    assert(s.isNarcissisticNumbers(0, 1))
    assert(s.getNarcissisticNumbers(1) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert(not(s.getNarcissisticNumbers(2)))
