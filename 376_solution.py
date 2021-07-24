"""
76. Binary Tree Path Sum
中文
English

Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.

A valid path is from root node to any of the leaf nodes.
Example

Example 1:

Input:
{1,2,4,2,3}
5
Output: [[1, 2, 2],[1, 4]]
Explanation:
The tree is look like this:
	     1
	    / \
	   2   4
	  / \
	 2   3
For sum = 5 , it is obviously 1 + 2 + 2 = 1 + 4 = 5

Example 2:

Input:
{1,2,4,2,3}
3
Output: []
Explanation:
The tree is look like this:
	     1
	    / \
	   2   4
	  / \
	 2   3
Notice we need to find all paths from root node to leaf nodes.
1 + 2 + 2 = 5, 1 + 2 + 3 = 6, 1 + 4 = 5 
There is no one satisfying it.
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
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        res = []
        self.transverse(root, target, "", res)
        return res

    def transverse(self, node, target, trail, res):
        if not node:
            if not target:
                res.append(list(map(int, trail.split(" ")[:-1])))
            return

        self.transverse(node.left, target-node.val, trail+str(node.val)+" ", res)
        self.transverse(node.right, target-node.val, trail+str(node.val)+" ", res)
if __name__ == "__main__":
    s = Solution()
