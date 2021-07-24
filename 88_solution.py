"""
88. Lowest Common Ancestor of a Binary Tree
中文
English

Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
Example

Example 1:

Input：{1},1,1
Output：1
Explanation：
 For the following binary tree（only one node）:
         1
 LCA(1,1) = 1

Example 2:

Input：{4,3,7,#,#,5,6},3,5
Output：4
Explanation：
 For the following binary tree:

      4
     / \
    3   7
       / \
      5   6
			
 LCA(3, 5) = 4

Notice

Assume two nodes are exist in tree.
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        pathA = self.search(root, A)
        pathB = self.search(root, B)
        lenA = len(pathA)
        lenB = len(pathB)
        print(pathA)
        print(pathB)
        for i in range(min(lenA, lenB)):
            print('a', pathA[lenA-1-i], lenA-1-i)
            print('b', pathB[lenB-1-i], lenB-1-i)
            if pathA[lenA-1-i] != pathB[lenB-1-i]:
                break
        node = root
        print('hi', pathA[lenA-i:][::-1])
        for char in pathA[lenA-i:][::-1]:
            if char == 'l':
                node = node.left
            elif char == 'r':
                node = node.right
            print(node.val, 'val')
        return node


    def search(self, node, target):
        if node == target:
            return 'f'
        if not node:
            return

        l = self.search(node.left, target)
        if l:
            return l + 'l'
        r = self.search(node.right, target)
        if r:
            return r + 'r'

        return

if __name__ == "__main__":
    s = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.right = n2
    n2.right = n3
    n3.right = n4
    n4.right = n5
    print(s.lowestCommonAncestor(n1, n3, n5).val)
