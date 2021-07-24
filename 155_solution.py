class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        return self.minCount(root)

    def minCount(self, node):
        if (not(node)):
            return 99999999999
        elif (not(node.left) and not(node.right)):
            return 1
        return min(self.minCount(node.left), self.minCount(node.right))+1

if (__name__ == "__main__"):
    s = Solution()
    n1 = TreeNode(0)
    n2 = TreeNode(1)
    n3 = TreeNode(2)
    n1.left = n2
    n1.right = n3
    print(s.minDepth(n1))
