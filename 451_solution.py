"""
451. Swap Nodes in Pairs
中文
English

Given a linked list, swap every two adjacent nodes and return its head.
Example

Example 1:

Input: 1->2->3->4->null
Output: 2->1->4->3->null

Example 2:

Input: 5->null
Output: 5->null

Challenge

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):
        if not(head.next):
            return head
        node = head
        head = head.next
        prev_node = None
        while node and node.next:
            next_node = node.next
            node.next = next_node.next
            next_node.next = node
            if prev_node:
                prev_node.next = next_node
            prev_node = node
            node = node.next
        return head

if __name__ == "__main__":
    s = Solution()
    l4 = ListNode(4)
    l3 = ListNode(3, l4)
    l2 = ListNode(2, l3)
    l1 = ListNode(1, l2)

    ans = s.swapPairs(l1)
    while ans:
        print(ans.val)
        ans = ans.next

    print()

    l7 = ListNode(3)
    l6 = ListNode(2, l7)
    l5 = ListNode(1, l6)
    ans = s.swapPairs(l5)
    while ans:
        print(ans.val)
        ans = ans.next
