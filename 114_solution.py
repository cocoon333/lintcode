"""
114. Unique Paths
中文
English

A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?
Example

Example 1:

Input: n = 1, m = 3
Output: 1	
Explanation: Only one path to target position.

Example 2:

Input:  n = 3, m = 3
Output: 6	
Explanation:
	D : Down
	R : Right
	1) DDRR
	2) DRDR
	3) DRRD
	4) RRDD
	5) RDRD
	6) RDDR

Notice

m and n will be at most 100.
"""

class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        l = [[1]*n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                l[i][j] = l[i-1][j] + l[i][j-1]
        return l[i][n-1]

if __name__ == "__main__":
    s = Solution()
    assert(s.uniquePaths(3, 1) == 1)
    assert(s.uniquePaths(3, 3) == 6)
