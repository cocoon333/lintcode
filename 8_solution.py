class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        offset = offset % len(s)
        return s[len(s) - offset:] + s[:len(s)-offset]

if (__name__ == "__main__"):
    s = Solution()
    print(s.rotateString("abcdefg", 3))
