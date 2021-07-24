"""
469. Same Tree
中文
English

Check if two binary trees are identical. Identical means the two binary trees have the same structure and every identical position has the same value.
Example

Example 1:

Input:{1,2,2,4},{1,2,2,4}
Output:true
Explanation:
        1                   1
       / \                 / \
      2   2   and         2   2
     /                   /
    4                   4

are identical.

Example 2:

Input:{1,2,3,4},{1,2,3,#,4}
Output:false
Explanation:

        1                  1
       / \                / \
      2   3   and        2   3
     /                        \
    4                          4

are not identical.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are identical, or false.
    """
    def isIdentical(self, a, b):
        la = []
        self.serialize(a, la)
        lb = []
        self.serialize(b, lb)
        return la == lb

    def serialize(self, node, res):
        if not node:
            res.append(None)
            return

        res.append(node.val)
        self.serialize(node.left, res)
        self.serialize(node.right, res)

if __name__ == "__main__":
    s = Solution()
