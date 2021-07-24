"""
170. Rotate List
中文
English

Given a list, rotate the list to the right by k places, where k is non-negative.
Example

Example 1:

Input:1->2->3->4->5  k = 2
Output:4->5->1->2->3

Example 2:

Input:3->2->1  k = 1
Output:1->3->2
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        if not(head and head.next):
            return head
        for i in range(k):
            prev = head.val
            node = head.next
            while node:
                temp = node.val
                node.val = prev
                prev = temp
                node = node.next
            head.val = prev
        return head

if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2, l1)
    l3 = ListNode(3, l2)
    l4 = ListNode(2, l3)
    l5 = ListNode(1, l4)

    node = s.rotateRight(l5, 1)
    while node:
        print(node.val)
        node = node.next

    print("test 2")
    l1 = ListNode(1)
    l2 = ListNode(0, l1)
    node = s.rotateRight(l2, 100)
    print(node.val, node.next.val)
