"""
109. Triangle
中文
English

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
Example

Example 1:

Input the following triangle:
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
Output: 11
Explanation: The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Example 2:

Input the following triangle:
[
     [2],
    [3,2],
   [6,5,7],
  [4,4,8,1]
]
Output: 12
Explanation: The minimum path sum from top to bottom is 12 (i.e., 2 + 2 + 7 + 1 = 12).

Notice

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        return self.helper(triangle, 0, 0, {})
        
    def helper(self, triangle, level, index, cache):
        if (level, index) in cache:
            return cache[(level, index)]
        if level == len(triangle):
            return 0
        path_sum = min(self.helper(triangle, level+1, index, cache), self.helper(triangle, level+1, index+1, cache))
        cache[(level, index)] = path_sum + triangle[level][index]
        return path_sum + triangle[level][index]

if __name__ == "__main__":
    s = Solution()
    assert(s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]) == 11)
    assert(s.minimumTotal([
     [2],
    [3,2],
   [6,5,7],
  [4,4,8,1]
]) == 12)
