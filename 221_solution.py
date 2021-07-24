"""
221. Add Two Numbers II

You have two numbers represented by linked list, where each node contains a single digit. The digits are stored in forward order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
Example

Example 1:

Input: 6->1->7   2->9->5
Output: 9->1->2

Example 2:

Input: 1->2->3   4->5->6
Output: 5->7->9
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param l1: The first list.
    @param l2: The second list.
    @return: the sum list of l1 and l2.
    """
    def addLists2(self, l1, l2):
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        carry = 0
        Dummy = ListNode(0)
        head = Dummy
        while l1 != None and l2 != None:
            sum = (l1.val + l2.val + carry) % 10
            carry = 1 if (l1.val + l2.val + carry) > 9 else 0
            head.next = ListNode(sum)
            head = head.next
            l1 = l1.next
            l2 = l2.next
            
        while l1 != None:
            sum = (l1.val + carry) % 10
            carry = 1 if l1.val + carry > 9 else 0
            head.next = ListNode(sum)
            l1 = l1.next
            head = head.next
        
        while l2 != None:
            sum = (l2.val + carry) % 10
            carry = 1 if l2.val + carry > 9 else 0
            head.next = ListNode(sum)
            l2 = l2.next
            head = head.next
        
        if carry:
            head.next = ListNode(carry)
        
        return self.reverse(Dummy.next)

    def reverse(self, head):
        if (not(head) or not(head.next)):
            return head
        past = None
        current = head
        future = head.next
        while (future.next):
            current.next = past
            past = current
            current = future
            future = future.next
        current.next = past
        future.next = current
        return future

if __name__ == "__main__":
    s = Solution()
    l3 = ListNode(2)
    l2 = ListNode(1, l3)
    l1 = ListNode(3, l2)

    l7 = ListNode(1)
    l6 = ListNode(5, l7)
    l5 = ListNode(9, l6)
    l4 = ListNode(5, l5)
    node = s.addLists2(l1, l4)
    while node:
        print(node.val)
        node = node.next
