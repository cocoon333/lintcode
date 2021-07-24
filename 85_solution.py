"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        if (not(root)):
            return node
        node_in_tree = root
        while (True):
            if (node.val > node_in_tree.val):
                new_node = node_in_tree.right
                if (not(new_node)):
                    node_in_tree.right = node
                    return root
                else:
                    node_in_tree = new_node
            elif (node.val < node_in_tree.val):
                new_node = node_in_tree.left
                if (not(new_node)):
                    node_in_tree.left = node
                    return root
                else:
                    node_in_tree = new_node
