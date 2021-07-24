"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        if (not(root)):
            return []
        node = root
        nodes = [root]
        res = []
        while (True):
            res.append(node.val)
            nodes.pop()
            if (node.right):
                print('here')
                nodes.append(node.right)
            if (node.left):
                print('here')
                nodes.append(node.left)
            if (not(len(nodes))):
                break
            node = nodes[-1]
        return res
