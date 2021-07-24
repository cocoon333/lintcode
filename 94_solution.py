"""
94. Binary Tree Maximum Path Sum

Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.
Example

Example 1:
	Input:  For the following binary tree（only one node）:
	2
	Output：2
	
Example 2:
	Input:  For the following binary tree:

      1
     / \
    2   3
		
	Output: 6
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
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        l = [-9999]
        res = self.helper(root, l)
        return max(l[0], res)

    def helper(self, root, possible_res):
        if not root:
            return -9999999
        if not(root.left or root.right):
            return root.val
        left_m = self.helper(root.left, possible_res)
        right_m = self.helper(root.right, possible_res)
        possible = max(root.val+left_m+right_m, root.val)
        if possible > possible_res[0]:
            possible_res[0] = possible
        return max(left_m+root.val, right_m+root.val, root.val)
