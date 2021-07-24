"""
98. Sort List
中文
English

Sort a linked list in O(n log n) time using constant space complexity.
Example

Example 1:

Input:  1->3->2->null
Output:  1->2->3->null

Example 2:

Input: 1->7->2->6->null
Output: 1->2->6->7->null	

Challenge

Solve it by merge sort & quick sort separately.
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
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        if not head:
            return head
        node = head
        l = []
        while node:
            l.append(node.val)
            node = node.next
        l.sort()
        node = ListNode(l[0])
        head = node
        for i in range(1, len(l)):
            node.next = ListNode(l[i])
            node = node.next

        return head
