"""
113. Remove Duplicates from Sorted List II
中文
English

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
Example

Example 1

Input : 1->2->3->3->4->4->5->null
Output : 1->2->5->null

Example 2

Input : 1->1->1->2->3->null
Output : 2->3->null
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
    @param head: head is the head of the linked list
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        if not head:
            return head
        prev = None
        node = head
        while node and node.next:
            end = node.next
            done = False
            while end and node.val == end.val:
                end = end.next
                done = True
            if done:
                if prev:
                    prev.next = end
                else:
                    head = end
            else:
                prev = node
            node = end
        return head

if __name__ == "__main__":
    s = Solution()
    test = [-14, -13, -12, -12, -11, -11, -11, -11, -11, -10, -10, -9, -9, -9, -8, -8, -7, -7, -6, -5, -5, -5, -5, -3, -3, -3, -3, -2, -1, -1, -1, -1, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 11, 11, 12, 12, 13, 13, 13,13, 13, 14, 14, 15, 15, 15, 16, 16, 16, 16, 17, 17, 17, 17, 18, 18, 18, 18, 19, 19, 21, 21, 21, 22, 23, 24, 25,25, 25, 25, 25]
    head = ListNode(test[0])
    node = head
    for i in range(1, len(test)):
        node.next = ListNode(test[i])
        node = node.next
    head = s.deleteDuplicates(head)
    while head:
        print(head)
        head = head.next
