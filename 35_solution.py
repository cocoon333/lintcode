class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        if (not(head)):
            return head
        past = None
        current = head
        future = head.next
        while (future.next):
            current.next = past
            past = current
            print('past', past.val)
            current = future
            print('current', current.val)
            future = future.next
            print('future', future.val)
        current.next = past
        future.next = current
        return future

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

if (__name__ == "__main__"):
    l5 = ListNode(5, None)
    l4 = ListNode(4, l5)
    l3 = ListNode(3, l4)
    l2 = ListNode(2, l3)
    l1 = ListNode(1, l2)
    s = Solution()
    print (s.reverse(l1).val)
    print (l5.val, l5.next.val)
    print (l4.val, l4.next.val)
    print (l3.val, l3.next.val)
    print (l2.val, l2.next.val)
    print (l1.val, l1.next)
