"""
1355. Pascal's Triangle
中文
English

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

图片
In Pascal's triangle, each number is the sum of the two numbers directly above it.
Example

Example 1:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

Example 2:

Input: 3
Output:
[
     [1],
    [1,1],
   [1,2,1]
]

"""
import math
class Solution:
    """
    @param numRows: num of rows
    @return: generate Pascal's triangle
    """
    def generate(self, numRows):
        res = [[1]]
        if numRows == 1:
            return res
        for i in range(1, numRows):
            res.append([])
            for j in range(i+1):
                res[-1].append(math.factorial(i)//math.factorial(j)//math.factorial(i-j))
        return res

if __name__ == "__main__":
    s = Solution()
    assert(s.generate(1) == [[1]])
    assert(s.generate(3) == [[1], [1, 1], [1, 2, 1]])
    assert(s.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])
