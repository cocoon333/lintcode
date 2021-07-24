"""
175. Invert Binary Tree
中文
English

Invert a binary tree.Left and right subtrees exchange.
Example

Example 1:

Input: {1,3,#}
Output: {1,#,3}
Explanation:
	  1    1
	 /  =>  \
	3        3

Example 2:

Input: {1,2,3,#,#,4}
Output: {1,3,2,#,4}
Explanation: 
	
      1         1
     / \       / \
    2   3  => 3   2
       /       \
      4         4

Challenge

Do it in recursion is acceptable, can you do it without recursion?
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        if root:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.invertBinaryTree(root.left)
            self.invertBinaryTree(root.right)

if __name__ == "__main__":
    s = Solution()
    t1 = TreeNode(1)
    t3 = TreeNode(3)
    t1.left = t3
    s.invertBinaryTree(t1)
    print (t1.val)
    print (t1.right.val)
    print (t1.left)
    t2 = TreeNode(2)
    t4 = TreeNode(4)

    t1.left = t2
    t3.left = t4
    s.invertBinaryTree(t1)
    print(t1.val)
    print(t1.left.val)
    print(t1.left.right.val)
    print(t1.right.val)
