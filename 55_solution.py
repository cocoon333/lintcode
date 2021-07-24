from collections import Counter
class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        dict_a = Counter(A)
        dict_b = Counter(B)
        for key in (dict_b.keys()):
            try:
                assert(dict_a[key] >= dict_b[key])
            except:
                return False
        return True

if (__name__ == "__main__"):
    s = Solution()
    assert(s.compareStrings("abc", "a"))
    assert(s.compareStrings("", ""))
    assert(not(s.compareStrings("abcdef", "z")))
    assert(not(s.compareStrings("abc", "aa")))
