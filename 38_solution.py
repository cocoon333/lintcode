"""
38. Search a 2D Matrix II
中文
English

Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it.

This matrix has the following properties:

    Integers in each row are sorted from left to right.
    Integers in each column are sorted from up to bottom.
    No duplicate integers in each row or column.

Example

Example 1:

Input:
	[[3,4]]
	target=3
Output:1

Example 2:

Input:
    [
      [1, 3, 5, 7],
      [2, 4, 7, 8],
      [3, 5, 9, 10]
    ]
    target = 3
Output:2

Challenge

O(m+n) time and O(1) extra space
"""

class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        count = 0
        for i in range(len(matrix[0])):
            if matrix[0][i] == target:
                count += 1
                break
            elif matrix[0][i] > target:
                i - 1
                break

        for j in range(1, len(matrix)):
            for k in range(i+1):
                if matrix[j][k] == target:
                    count += 1
                    break
                elif matrix[j][k] > target:
                    break
        return count

if __name__ == "__main__":
    s = Solution()
    assert(s.searchMatrix([[3,4]], 3) == 1)
    assert(s.searchMatrix([
      [1, 3, 5, 7],
      [2, 4, 7, 8],
      [3, 5, 9, 10]
    ], 3) == 2)
