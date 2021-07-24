class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        res = []
        self.postorderTraversa(root, res)  
        return res
  
    def postorderTraversa(self, node, res):
        if (node): 
            self.postorderTraversa(node.left, res)
            self.postorderTraversa(node.right, res)
            res.append(node.val)
