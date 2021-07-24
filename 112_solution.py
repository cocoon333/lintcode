"""
112. Remove Duplicates from Sorted List
中文
English

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example

Example 1:
	Input:  null
	Output: null


Example 2:
	Input:  1->1->2->null
	Output: 1->2->null
	
Example 3:
	Input:  1->1->2->3->3->null
	Output: 1->2->3->null
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
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        node = head
        while node:
            if (node.next and node.next.val == node.val):
                node.next = node.next.next
            else:
                node = node.next
        return head

