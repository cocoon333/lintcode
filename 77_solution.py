"""
77. Longest Common Subsequence
中文
English

Given two strings, find the longest common subsequence (LCS).

Your code should return the length of LCS.
Example

Example 1:
	Input:  "ABCD" and "EDCA"
	Output:  1
	
	Explanation:
	LCS is 'A' or  'D' or 'C'


Example 2:
	Input: "ABCD" and "EACB"
	Output:  2
	
	Explanation: 
	LCS is "AC"

Clarification

What's the definition of Longest Common Subsequence?

    https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
    http://baike.baidu.com/view/2020307.htm
"""

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        if not (A and B):
            return 0
        a = len(A)
        b = len(B)
        res = [[0] * (b+1) for i in range(a+1)]
        for i in range(1, a+1):
            for j in range(1, b+1):
                res[i][j] = max(res[i-1][j], res[i][j-1])
                if A[i-1] == B[j-1]:
                    res[i][j] = max(res[i-1][j-1] + 1, res[i][j])
        for i in range(a):
            print(res[i])
        return res[i][j]

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonSubsequence("daabeddbcedeabcbcbec", "daceeaeeaabbabbacedd"))
    """
    assert(s.longestCommonSubsequence("bedaacbade", "dccaeedbeb") == 5)
    assert(s.longestCommonSubsequence("ABCD", "EDCA") == 1)
    assert(s.longestCommonSubsequence("ABCD", "EACB") == 2)
    """
