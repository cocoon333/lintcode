class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        max_count = 0
        i = 0
        for i in range(len(A)):
            count = 0
            pointer = i
            for j in range(len(B)):
                if (A[pointer] == B[j]):
                    count += 1
                    if (pointer < len(A) - 1):
                        pointer += 1
                    elif(count > max_count):
                        return count
                elif (count > 0):
                    if (count > max_count):
                        max_count = count
                    count = 0 
                    pointer = i
            if (count > max_count):
                max_count = count
        return max_count

if (__name__ == "__main__"):
    s = Solution()
    assert(s.longestCommonSubstring("abccccccccccde", "dbccccccabccde"))
    assert(s.longestCommonSubstring("abcdefgh", "abc") == 3)
    assert(s.longestCommonSubstring("abcdefgh", "efg") == 3)
    assert(s.longestCommonSubstring("abcdefgh", "123") == 0)
    assert(s.longestCommonSubstring("123", "123456789") == 3)
    assert(s.longestCommonSubstring("", "abc") == 0)
    assert(s.longestCommonSubstring("abc", "") == 0)
    assert(s.longestCommonSubstring("banana", "cianaic") == 3)
    assert(s.longestCommonSubstring("cianaic", "banana") == 3)
    assert(s.longestCommonSubstring("www.placeholder.com code", "www.othername.com code") == 9)
