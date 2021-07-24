"""
434. Number of Islands II

Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). Originally, the 2D matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island. Return how many island are there in the matrix after each operator.
Example

Example 1:

Input: n = 4, m = 5, A = [[1,1],[0,1],[3,3],[3,4]]
Output: [1,1,2,2]
Explanation:
0.  00000
    00000
    00000
    00000
1.  00000
    01000
    00000
    00000
2.  01000
    01000
    00000
    00000
3.  01000
    01000
    00000
    00010
4.  01000
    01000
    00000
    00011

Example 2:

Input: n = 3, m = 3, A = [[0,0],[0,1],[2,2],[2,1]]
Output: [1,1,2,2]

Notice

0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.
"""
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        cache = set()
        count = [0]
        for op in operators:
            if ((op[0]-1, op[1]) in cache):
                count.append([-1]+1)
                cache.add(op)
            elif ((op[0]+1, op[1]) in cache):
                count.append([-1]+1)
                cache.add(op)
            elif ((op[0], op[1]-1) in cache):
                count.append([-1]+1)
                cache.add(op)
            elif ((op[0]+1, op[1]+1) in cache):
                count.append([-1]+1)
                cache.add(op)
            else:
                count.append([-1])
                cache.add(op)
        return count
