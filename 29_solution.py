"""
29. Interleaving String
中文
English

Given three strings: s1, s2, s3, determine whether s3 is formed by the interleaving of s1 and s2.
Example

Example 1:

Input:
"aabcc"
"dbbca"
"aadbbcbcac"
Output:
true

Example 2:

Input:
""
""
"1"
Output:
false

Example 3:

Input:
"aabcc"
"dbbca"
"aadbbbaccc"
Output:
false

Challenge

O(n2) time or better
"""

class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        return self.helper(s1, 0, s2, 0, s3, 0)

    def helper(self, s1, i, s2, j, s3, k):
        if k == len(s3):
            return True

        any_s1_left = i < len(s1)
        any_s2_left = j < len(s2)
        if any_s1_left and any_s2_left and s1[i] == s2[j] == s3[k]:
            return self.helper(s1, i+1, s2, j, s3, k+1) or self.helper(s1, i, s2, j+1, s3, k+1)
        elif any_s1_left and s1[i] == s3[k]:
            return self.helper(s1, i+1, s2, j, s3, k+1)
        elif any_s2_left and s2[j] == s3[k]:
            return self.helper(s1, i, s2, j+1, s3, k+1)
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    assert(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
    assert(not s.isInterleave("", "", "1"))
    assert(not s.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
