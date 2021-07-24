import re
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        s = s.lower()
        start = 0
        end = len(s)-1
        while (start < end):
            if (not(re.search('[a-z0-9]', s[start]))):
                start += 1
                continue
            if (not(re.search('[a-z0-9]', s[end]))):
                end -= 1
                continue
            if (s[start] != s[end]):
                return False
            start += 1
            end -= 1
        return True

if (__name__ == "__main__"):
    s = Solution()
    assert(s.isPalindrome("aba"))
    assert(s.isPalindrome("a"))
    assert(s.isPalindrome("d d d"))
    assert(s.isPalindrome("a :#@!( a"))
    assert(s.isPalindrome("zazazaz"))
    assert(not(s.isPalindrome("zaxzazaz")))
    assert(not(s.isPalindrome("za:zzz")))
    assert(not(s.isPalindrome("1a2")))
