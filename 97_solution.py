"""
97. Maximum Depth of Binary Tree
中文
English

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Example

Example 1:

Input: tree = {}
Output: 0
Explanation: The height of empty tree is 0.

Example 2:

Input: tree = {1,2,3,#,#,4,5}
Output: 3	
Explanation: Like this:
   1
  / \                
 2   3                
    / \                
   4   5
it will be serialized {1,2,3,#,#,4,5}
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        return self.maxDepthHelper(root, 0)

    def maxDepthHelper(self, node, max_l):
        if (node):
            max_l += 1
            return max(self.maxDepthHelper(node.left, max_l), self.maxDepthHelper(node.right, max_l))
        return max_l

if __name__ == "__main__":
    s = Solution()
    t1 = TreeNode(0)
    assert(s.maxDepth(t1) == 1)
    assert(s.maxDepth(None) == 0)

