"""
76. Longest Increasing Subsequence
中文
English

Given a sequence of integers, find the longest increasing subsequence (LIS).

You code should return the length of the LIS.
Example

Example 1:
	Input:  [5,4,1,2,3]
	Output:  3
	
	Explanation:
	LIS is [1,2,3]


Example 2:
	Input: [4,2,4,5,3,7]
	Output:  4
	
	Explanation: 
	LIS is [2,4,5,7]

Challenge

Time complexity O(n^2) or O(nlogn)
Clarification

What's the definition of longest increasing subsequence?

    The longest increasing subsequence problem is to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique.

    https://en.wikipedia.org/wiki/Longest_increasing_subsequence
"""

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and res[i] <= res[j]:
                    res[i] = res[j] + 1
        return max(res)


if __name__ == "__main__":
    s = Solution()
    assert(s.longestIncreasingSubsequence([5,4,1,2,3]) == 3)
    assert(s.longestIncreasingSubsequence([4,2,4,5,3,7]) == 4)
    assert(s.longestIncreasingSubsequence([9,3,6,2,7]) == 3)
