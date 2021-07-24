"""
11. Search Range in Binary Search Tree
中文
English

Given a binary search tree and a range [k1, k2], return node values within a given range in ascending order.
Example

Example 1:

Input：{5},6,10
Output：[]
        5
it will be serialized {5}
No number between 6 and 10

Example 2:

Input：{20,8,22,4,12},10,22
Output：[12,20,22]
Explanation：
        20
       /  \
      8   22
     / \
    4   12
it will be serialized {20,8,22,4,12}
[12,20,22] between 10 and 22
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
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        res = []
        self.helper(root, k1, k2, res)
        return res

    def helper(self, node, min_n, max_n, res):
        if not node:
            return
        elif node.val >= min_n and node.val <= max_n:
            res.append(node.val)
            self.helper(node.left, min_n, max_n, res)
            self.helper(node.right, min_n, max_n, res)
        elif node.val >= min_n:
            self.helper(node.left, min_n, max_n, res)
        elif node.val <= max_n:
            self.helper(node.right, min_n, max_n, res)
