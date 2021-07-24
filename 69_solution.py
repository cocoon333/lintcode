"""
69. Binary Tree Level Order Traversal
中文
English

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
Example

Example 1:

Input：{1,2,3}
Output：[[1],[2,3]]
Explanation：
  1
 / \
2   3
it will be serialized {1,2,3}
level order traversal

Example 2:

Input：{1,#,2,3}
Output：[[1],[2],[3]]
Explanation：
1
 \
  2
 /
3
it will be serialized {1,#,2,3}
level order traversal

Challenge

Challenge 1: Using only 1 queue to implement it.

Challenge 2: Use BFS algorithm to do it.
Notice

    The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
    The number of nodes does not exceed 20.

"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def levelOrder(self, root):
        res = []
        nodes = [root]
        if (not(root)):
            return res
        while nodes:
            res.append([])
            new_nodes = []
            for node in nodes:
                if node:
                    res[-1].append(node.val)
                    new_nodes.append(node.left)
                    new_nodes.append(node.right)
            nodes = new_nodes
        return res[:len(res)-1]

if __name__ == "__main__":
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.left = t2
    t1.right = t3
    print(s.levelOrder(t1))
