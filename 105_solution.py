"""
105. Copy List with Random Pointer
中文
English

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
Challenge

Could you solve it with O(1) space?
"""

"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""

class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        cache = {}
        new_node = None
        prev = None
        node = head
        while node:
            new_node = RandomListNode(node.label)
            cache[node.label] = new_node
            if prev:
                prev.next = new_node
            prev = new_node
            node = node.next

        node = head
        new_node = cache[node.label]
        while node:
            if node.random:
                new_node.random = cache[node.random.label]
            node = node.next
            new_node = new_node.next

        return cache[head.label]
