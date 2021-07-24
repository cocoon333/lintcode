"""
397. Longest Continuous Increasing Subsequence
中文
English

Give an integer array，find the longest increasing continuous subsequence in this array.

An increasing continuous subsequence:

    Can be from right to left or from left to right.
    Indices of the integers in the subsequence should be continuous.

Example

Example 1:

Input: [5, 4, 2, 1, 3]
Output: 4
Explanation:
For [5, 4, 2, 1, 3], the LICS  is [5, 4, 2, 1], return 4.

Example 2:

Input: [5, 1, 2, 3, 4]
Output: 4
Explanation:
For [5, 1, 2, 3, 4], the LICS  is [1, 2, 3, 4], return 4.

Challenge

O(n) time and O(1) extra space.
"""
class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        if not A:
            return 0
        max_count = 0
        count = 1
        for i in range(len(A)-1):
            if A[i] < A[i+1]:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 1

        if count > max_count:
            max_count = count
        count = 1

        
        for i in range(len(A)-1, 0, -1):
            if A[i] < A[i-1]:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 1 

        if count > max_count:
            max_count = count
        count = 1

        return max_count

if __name__ == "__main__":
    s = Solution()
    assert(s.longestIncreasingContinuousSubsequence([5, 4, 2, 1, 3]) == 4)
    assert(s.longestIncreasingContinuousSubsequence([5, 1, 2, 3, 4]) == 4)
