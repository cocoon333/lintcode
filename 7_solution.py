class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def serialize(self, root):
        if (not(root)):
            return []
        res = [root.val]
        nodes = [root]
        while (nodes):
            if (nodes[0]):
                self.tranverse(nodes[0], res)
                nodes.append(nodes[0].left)
                nodes.append(nodes[0].right)
            nodes.pop(0)
        if (res[-1] == "#"):
            res.pop()
        return res

    def tranverse(self, node, res):
        if (not(node.left or node.right)):
                return
        if (node.left):
            res.append(node.left.val)
        else:
            res.append("#")
        if (node.right):
            res.append(node.right.val)
        else:
            res.append("#")
        

    def deserialize(self, serial):
        serial.reverse()
        return _deserialize(serial)

    def _deserialize(serial):
        if (not(serial)):
            return None

        node = None
        value = serial.pop()
        if (value != '#'):
            node = Node(value)
            node.left = _deserialize(serial)
            node.right = _deserialize(serial)
        return node

if (__name__ == "__main__"):
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    print(s.serialize(t1))
    print(s.serialize([]))
    t1.left = t2
    t1.right = t3
    print(s.serialize(t1))
    t2.left = t4
    t4.left = t5
    print(s.serialize(t1))
    t3.right = t6
    print(s.serialize(t1))
