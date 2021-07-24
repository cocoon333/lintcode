class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        if (not(root)):
            return []
        node = root
        nodes = [root]
        res = []
        while (True):
            if (not(node.left)):
                res.append(node)
                nodes.pop()
            if (node.right):
                print('here')
                nodes.append(node.right)
            if (node.left):
                print('herel')
                nodes.append(node.left)
            if (not(len(nodes))):
                break
            node = nodes[-1]
        return res

