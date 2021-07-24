"""
174. Remove Nth Node From End of List
中文
English

Given a linked list, remove the nth node from the end of list and return its head.
Example

Example 1:
	Input: list = 1->2->3->4->5->null， n = 2
	Output: 1->2->3->5->null


Example 2:
	Input:  list = 5->4->3->2->1->null, n = 2
	Output: 5->4->3->1->null

Challenge

Can you do it without getting the length of the linked list?
Notice

The minimum number of nodes in list is n.
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        if self.helper(head, n, 0) < n:
            return head.next
        return head

    def helper(self, node, n, i):
        if not node.next:
            return i
        i = self.helper(node.next, n, i) + 1
        if i == n:
            node.next = node.next.next
        return i

if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(5)
    l2 = ListNode(4, l1)
    l3 = ListNode(3, l2)
    l4 = ListNode(2, l3)
    l5 = ListNode(1, l4)
    
    l6 = ListNode(1)
    l7 = ListNode(2, l6)
    l8 = ListNode(3, l7)
    l9 = ListNode(4, l8)
    l10 = ListNode(5, l9)

    h1 = s.removeNthFromEnd(l5, 2)
    h2 = s.removeNthFromEnd(l10, 2)
    h3 = s.removeNthFromEnd(l5, 4)

    print("h1")

    while h1:
        print(h1.val)
        h1 = h1.next

    print("h2")

    while h2:
        print(h2.val)
        h2 = h2.next

    print("h3")

    while h3:
        print(h3.val)
        h3 = h3.next
