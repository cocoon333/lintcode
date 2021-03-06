"""
102. Linked List Cycle
中文
English

Given a linked list, determine if it has a cycle in it.


Example

	Example 1:
		Input: 21->10->4->5,  then tail connects to node index 1(value 10).
		Output: true
		
	Example 2:
		Input: 21->10->4->5->null
		Output: false
	
	```

Challenge

Follow up:
Can you solve it without using extra space?
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
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next

        return False
