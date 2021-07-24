"""
433. Number of Islands
中文
English

Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Find the number of islands.
Example

Example 1:

Input:
[
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
Output:
3

Example 2:

Input:
[
  [1,1]
]
Output:
1
"""

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.deleteIslands(i, j, grid)
                    count += 1
        return count

    def deleteIslands(self, i, j, grid):
        if grid[i][j] == 0:
            return
        grid[i][j] = 0
        if i > 0:
            self.deleteIslands(i-1, j, grid)
        if j > 0:
            self.deleteIslands(i, j-1, grid)
        if i < len(grid)-1:
            self.deleteIslands(i+1, j, grid)
        if j < len(grid[0])-1:
            self.deleteIslands(i, j+1, grid)

if __name__ == "__main__":
    s = Solution()
    print(s.numIslands([[1, 1]]))
    print(s.numIslands([
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
))
