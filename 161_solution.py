"""
161. Rotate Image
中文
English

You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Example

Example 1：

Input:[[1,2],[3,4]]
Output:[[3,1],[4,2]]

Example 2:

Input:[[1,2,3],
       [4,5,6],
       [7,8,9]]
Output:[[7,4,1],[8,5,2],[9,6,3]]

Challenge

Do it in-place.
"""

class Solution:
    """
    @param matrix: a lists of integers
    @return: nothing
    """
    def rotate(self, matrix):
        for i in range(3):
            self.transpose(matrix)
            self.reverse(matrix)
        return matrix

    def transpose(self, matrix):
        for i in range(len(matrix)):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

    def reverse(self, matrix):
        for j in range(len(matrix)):
            start = 0
            end = len(matrix)-1
            while start < end:
                temp = matrix[start][j]
                matrix[start][j] = matrix[end][j]
                matrix[end][j] = temp
                start += 1
                end -= 1

if __name__ == "__main__":
    s = Solution()
    assert(s.rotate([[1, 2], [3, 4]]) == [[3, 1], [4, 2]])
    print(s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
