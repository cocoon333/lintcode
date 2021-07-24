"""
1195. Find Largest Value in Each Tree Row
中文
English

You need to find the largest value in each row of a binary tree.
Example

Example 1:

Input:
{1,3,2,5,3,#,9}
Output:
[1,3,9]

Explanation:
     1
   /    \
  3     2
 /   \     \
5    3      9

Example 2:

Input:
{1,2,3,4,5,6,#,#,7}
Output:
[1,3,6,7]

Explanation:
           1
        /     \
     2         3
   /  \      /
 4    5   6
  \
   7
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
    @param root: a root of integer
    @return: return a list of integer
    """
    def largestValues(self, root):
        level_transversal = []
        res = []
        self.helper(root, level_transversal, 0)
        for i in range(len(level_transversal)):
            res.append(max(level_transversal[i]))
        return res

    def helper(self, node, res, level):
        if not(node):
            return
        
        if level == len(res):
            res.append([])

        res[level].append(node.val)
        self.helper(node.left, res, level+1)
        self.helper(node.right, res, level+1)
