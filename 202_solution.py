"""
202. Segment Tree Query

For an integer array (index from 0 to n-1, where n is the size of this array), in the corresponding SegmentTree, each node stores an extra attribute max to denote the maximum number in the interval of the array (index from start to end).

Design a query method with three parameters root, start and end, find the maximum number in the interval [start, end] by the given root of segment tree.
Example

Example 1:

Input："[0,3,max=4][0,1,max=4][2,3,max=3][0,0,max=1][1,1,max=4][2,2,max=2][3,3,max=3]",1,2
Output：4
Explanation：
For array [1, 4, 2, 3], the corresponding Segment Tree is :

	                  [0, 3, max=4]
	                 /             \
	          [0,1,max=4]        [2,3,max=3]
	          /         \        /         \
	   [0,0,max=1] [1,1,max=4] [2,2,max=2], [3,3,max=3]
The maximum value of [1,2] interval is 4

Example 2:

Input："[0,3,max=4][0,1,max=4][2,3,max=3][0,0,max=1][1,1,max=4][2,2,max=2][3,3,max=3]",2,3
Output：3
Explanation：
For array [1, 4, 2, 3], the corresponding Segment Tree is :

	                  [0, 3, max=4]
	                 /             \
	          [0,1,max=4]        [2,3,max=3]
	          /         \        /         \
	   [0,0,max=1] [1,1,max=4] [2,2,max=2], [3,3,max=3]
The maximum value of [2,3] interval is 3

Notice

It is much easier to understand this problem if you finished Segment Tree Build first.
"""

class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of segment tree.
    @param start: start value.
    @param end: end value.
    @return: The maximum number in the interval [start, end]
    """
    def query(self, root, start, end):
        return self.helper(root, start, end)
    
    def helper(self, node, start, end):
        max_num = -9999
        max_l = -9999
        max_r = -9999
        left = False
        right = False
        print('node', node.start, node.end, node.max)
        if start <= node.start and end >= node.end:
            return node.max
        else:
            if end < node.end and node.left:
                print('left')
                left = True
                max_l = self.helper(node.left, start, end)
            if start > node.start and node.right:
                right = True
                max_r = self.helper(node.right, start, end)
            if start == node.start or end == node.end:
                if not left:
                    max_l = self.helper(node.left, start, end)
                elif not right:
                    max_r = self.helper(node.right, start, end)
        return max(max_l, max_r)

if __name__ == "__main__":
    s = Solution()
    n1 = SegmentTreeNode(0, 3, 4)
    n2 = SegmentTreeNode(0, 1, 4)
    n3 = SegmentTreeNode(2, 3, 3)
    n4 = SegmentTreeNode(0, 0, 1)
    n5 = SegmentTreeNode(1, 1, 4)
    n6 = SegmentTreeNode(2, 2, 2)
    n7 = SegmentTreeNode(3, 3, 3)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    
    print('answer', s.query(n1, 2, 3))
    print('answer', s.query(n1, 1, 3))
    print('answer', s.query(n1, 0, 1))
