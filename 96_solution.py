"""
96. Partition List
中文
English

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
Example

Example 1:

Input:  list = null, x = 0
Output: null
Explanation: The empty list Satisfy the conditions by itself.

Example 2:

Input:  list = 1->4->3->2->5->2->null, x = 3
Output: 1->2->2->4->3->5->null
Explanation:  keep the original relative order of the nodes in each of the two partitions.
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution(object):
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        if not(head):
            return head
        l = []
        node = head
        while (node):
            l.append(node)
            node = node.next
        print(l)
        i = 0
        j = 0
        while (i < len(l) and j < len(l)):
            while(l[i].val < x):
                i += 1
                print('i', i)
            while(l[j].val >= x):
                j += 1
                print('j', j)
            self.swap(l, i, j)
        
        for i in range(len(l)-1):
            l[i].next = l[i+1]
        l[-1].next = None
        return l[0]

    def partition(self, head, x):
        if not(head):
            return head
        fsmaller = ListNode(0)
        flarger = ListNode(0)
        larger = flarger
        smaller = fsmaller
        node = head
        while node:
            if node.val < x:
                smaller.next = node
                smaller = smaller.next
            else:
                larger.next = node
                larger = larger.next
            node = node.next
        larger.next = None
        smaller.next = flarger.next
        return fsmaller.next

    def swap(self, l, i, j):
        temp = l[i]
        l[i] = l[j]
        l[j] = temp

if (__name__ == "__main__"):
    s = Solution()
#    l1 = ListNode(1)
#    print(s.partition(l1, 0).val)

    l5 = ListNode(4)
    l4 = ListNode(2, l5)
    l3 = ListNode(1, l4)
    l2 = ListNode(3, l3)
    l1 = ListNode(3, l2)
    node = s.partition(l1, 3)
    while (node):
        print (node.val)
        node = node.next
