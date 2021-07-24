"""
115. Unique Paths II
中文
English

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.
Example

Example 1:
	Input: [[0]]
	Output: 1


Example 2:
	Input:  [[0,0,0],[0,1,0],[0,0,0]]
	Output: 2
	
	Explanation:
	Only 2 different path.
	

Notice

m and n will be at most 100.
"""
class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0
        res = [[0]*len(obstacleGrid[0]) for i in range(len(obstacleGrid))]
        res[0][0] = 1
        for i in range(len(res)):
            for j in range(len(res[0])):
                if obstacleGrid[i][j]:
                    continue
                if i > 0 and not obstacleGrid[i-1][j]:
                    res[i][j] += res[i-1][j]
                if j > 0 and not obstacleGrid[i][j-1]:
                    res[i][j] += res[i][j-1]

        return res[i][j]

if __name__ == "__main__":
    s = Solution()
    assert(s.uniquePathsWithObstacles([[0]]) == 1)
    assert(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]) == 2)
    assert(s.uniquePathsWithObstacles([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[1,0,0,0,0,0,0,0,0,1]]) == 0)
