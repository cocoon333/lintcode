"""
104. Merge K Sorted Lists
中文
English

Merge k sorted linked lists and return it as one sorted list.

Analyze and describe its complexity.
Example

Example 1:
	Input:   [2->4->null,null,-1->null]
	Output:  -1->2->4->null

Example 2:
	Input: [2->6->null,5->null,7->null]
	Output:  2->5->6->7->null
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
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        if not lists:
            return None

        res = []
        for node in lists:
            while node:
                res.append(node.val)
        res.sort()
        head = ListNode(res[0])
        node = head
        for i in range(len(res)-1):
            node.next = ListNode(res[i+1])
            node = node.next
        return head
