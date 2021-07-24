"""
110. Minimum Path Sum
中文
English

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Example

Example 1:
	Input:  [[1,3,1],[1,5,1],[4,2,1]]
	Output: 7
	
	Explanation:
	Path is: 1 -> 3 -> 1 -> 1 -> 1


Example 2:
	Input:  [[1,3,2]]
	Output: 6
	
	Explanation:  
	Path is: 1 -> 3 -> 2

Notice

You can only go right or down in the path..
"""

class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        res = []
        for i in range(len(grid)):
            res.append([0] * len(grid[0]))
        res[0][0] = grid[0][0]
        for i in range(len(grid)):
            if i > 0:
                res[i][0] = res[i-1][0] + grid[i][0]

        for j in range(len(grid[0])):
            if j > 0:
                res[0][j] = res[0][j-1] + grid[0][j]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                if res[i-1][j] < res[i][j-1]:
                    res[i][j] = res[i-1][j] + grid[i][j]
                else:
                    res[i][j] = res[i][j-1] + grid[i][j]
        return res[-1][-1]

if __name__ == "__main__":
    s = Solution()
    assert(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]) == 7)
    assert(s.minPathSum([[1,3,2]]) == 6)
