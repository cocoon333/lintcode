"""
452. Remove Linked List Elements
中文
English

Remove all elements from a linked list of integers that have value val.
Example

Example 1:

Input: head = 1->2->3->3->4->5->3->null, val = 3
Output: 1->2->4->5->null

Example 2:

Input: head = 1->1->null, val = 1
Output: null

"""

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        while head and head.val == val:
            head = head.next
        if not head:
            return None

        prev_node = head
        node = head.next
        while node:
            if node.val == val:
                prev_node.next = node.next
            node = node.next

        return head
