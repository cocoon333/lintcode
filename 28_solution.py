class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if (not(matrix)):
            return False
        index = self.findItem(matrix[self.findRow(matrix, target, 0, len(matrix)-1)], target, 0, len(matrix[0]))
        if (index >= 0):
            return True
        else:
            return False

    def findRow(self, matrix, target, left, right):
        if (right-left <= 1):
            if (matrix[right][0] <= target):
                return (right)
            else:
                return left
        if (target <= matrix[(left+right)//2][0]):
            return self.findRow(matrix, target, left, (left+right)//2)
        else:
            return self.findRow(matrix, target, (left+right)//2, right)

    def findItem(self, matrix, target, left, right):
        if (right-left <= 1):
            if (matrix[left] == target):
                return (left)
            else:
                return -1
        if (target < matrix[(left+right)//2]):
            return self.findItem(matrix, target, left, (left+right)//2)
        else:
            return self.findItem(matrix, target, (left+right)//2, right)

if (__name__ == "__main__"):
    s = Solution()
    print(s.searchMatrix([[1, 4, 5], [6, 7, 8]], 6))
    print(s.searchMatrix([[1, 4, 5], [6, 7, 8]], 1))
    print(s.searchMatrix([[1]], 1))
    print(s.searchMatrix([[3]], 1))
