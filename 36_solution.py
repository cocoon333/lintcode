"""
36. Reverse Linked List II
中文
English

Reverse a linked list from position m to n.
Example

Example 1:

Input: 1->2->3->4->5->NULL, m = 2 and n = 4, 
Output: 1->4->3->2->5->NULL.

Example 2:

Input: 1->2->3->4->NULL, m = 2 and n = 3, 
Output: 1->3->2->4->NULL.

Challenge

Reverse it in-place and in one-pass
Notice

Given m, n satisfy the following condition: 1 ≤ m ≤ n ≤ length of list.
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()

class Solution:
    """
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        for i in range(1, m):
            head = head.next

        print('head', head)
        prev = head
        curr = head.next
        tail = head.next
        prev.next = None
        for i in range(m, n+1):
            if i == n:
                print("hi")
                print(tail.next, curr.next)
                tail.next = curr.next

            temp = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = temp
            print('curr', curr, curr.next)
            print('prev', prev, prev.next)
        return dummy.next

if __name__ == "__main__":
    s = Solution()
    l5 = ListNode(5)
    l4 = ListNode(4, l5)
    l3 = ListNode(3, l4)
    l2 = ListNode(2, l3)
    l1 = ListNode(1, l2)
    head = s.reverseBetween(l1, 2, 4)
    i = 0
    while head and i < 10:
        print(head.val)
        head = head.next
        i += 1
