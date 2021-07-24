"""
162. Set Matrix Zeroes
中文
English

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
Example

Example 1:

Input:[[1,2],[0,3]]
Output:[[0,2],[0,0]]

Example 2:

Input:[[1,2,3],[4,0,6],[7,8,9]]
Output:[[1,0,3],[0,0,0],[7,0,9]]

Challenge

Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

class Solution:
    """
    @param matrix: A lsit of lists of integers
    @return: nothing
    """
    def setZeroes(self, matrix):
        prev = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not(matrix[i][j]) and not(i in prev and j in prev[i]):
                    print('i', i)
                    print('j', j)
                    print()
                    self.setZero(i, j, matrix, prev)

    def setZero(self, i, j, matrix, prev):
        for k in range(len(matrix)):
            if matrix[k][j]:
                if k in prev:
                    prev[k].append(j)
                else:
                    prev[k] = [j]
            matrix[k][j] = 0

        for a in range(len(matrix[0])):
            if matrix[i][a]:
                if i in prev:
                    prev[i].append(a)
                else:
                    prev[i] = [a]

            matrix[i][a] = 0

if __name__ == "__main__":
    l = [[1, 2], [0, 3]]
    l2 = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    l3 = [[-4       ,-2147483648, 6,-7, 0],
          [-8,        6,         -8,-6, 0],
          [2147483647,2,         -9,-6,-10]]
    l4 = [[8,3,8,7,3],[3,2,3,2,2],[9,9,5,6,1],[2,0,8,2,6],[1,9,4,2,8],[4,5,9,4,6],[3,4,1,2,4],[4,7,8,7,0],[0,8,1,8,5],[2,0,7,3,4]]
    s = Solution()
    s.setZeroes(l)
    s.setZeroes([])
    s.setZeroes(l2)
    s.setZeroes(l3)
    s.setZeroes(l4)
    assert(l == [[0, 2], [0, 0]])
    assert(l2 == [[1, 0, 3], [0, 0, 0], [7, 0, 9]])
    assert(l3 == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [2147483647, 2, -9, -6, 0]])
    print(l4)
