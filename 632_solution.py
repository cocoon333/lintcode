class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """
    def maxNode(self, root):
        l = self.maxN(root.left())
        r = self.maxN(root.right())
        return self.merge(l, r)
        
    def maxN(self, node):
        if (not(node.left())):
            return node.val
        l = self.maxN(root.left())
        r = self.maxN(root.right())
        return self.merge(l, r)
        
    def merge(self, l, r)
        if(l.val > r.val):
            return l.val
        else:
            return r.val
