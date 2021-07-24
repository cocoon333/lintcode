"""
185. Matrix Zigzag Traversal
中文
English

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in ZigZag-order.
Example

Example 1:
	Input: [[1]]
	Output:  [1]

Example 2:
	Input:   
	[
    [1, 2,  3,  4],
    [5, 6,  7,  8],
    [9,10, 11, 12]
  ]

	Output:  [1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12]
"""

class Solution:
    """
    @param matrix: An array of integers
    @return: An array of integers
    """
    def printZMatrix(self, matrix):
        res = []
        for i in range(len(matrix)):
            l = ([None] * i)
            l.extend(matrix[i])
            matrix[i] = l

        for j in range(len(matrix[-1])):
            if j % 2:
                for i in range(len(matrix)):
                    if len(matrix[i]) < j+1:
                        continue
                    if matrix[i][j] != None:
                        res.append(matrix[i][j])
            else:
                for i in range(len(matrix)-1, -1, -1):
                    if len(matrix[i]) < j+1:
                        continue
                    if matrix[i][j] != None:
                       res.append(matrix[i][j])

        return res

if __name__ == "__main__":
    s = Solution()
    assert(s.printZMatrix([[1]]) == [1])
    assert(s.printZMatrix( [
    [1, 2,  3,  4],
    [5, 6,  7,  8],
    [9,10, 11, 12]
  ]) ==  [1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12])
