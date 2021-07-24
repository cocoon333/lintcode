class Solution:
    """
    @param k: An integer
    @param n: An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCounts(self, k, n):
        all_digits = []
        for i in range(n+1):
            all_digits.extend(self.digits(i))
        return all_digits.count(k)

    def digits(self, num):
        return [int(d) for d in str(num)]

if (__name__ == "__main__"):
    s = Solution()
#    assert(s.digits(123) == [1, 2, 3])
#    assert(s.digits(1) == [1])
#    assert(s.digits(11) == [1, 1])
#    assert(s.digitCounts(1, 1) == 1)
#    assert(s.digitCounts(1, 12) == 5)
#    print(s.digitCounts(1, 112))
    print(s.digitCounts(1, 10000))
    print(s.digits(10000))

