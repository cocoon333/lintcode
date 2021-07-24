"""
173. Insertion Sort List

Sort a linked list using insertion sort.
Example

Example 1:
	Input: 0->null
	Output: 0->null


Example 2:
	Input:  1->3->2->0->null
	Output :0->1->2->3->null
	
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        if not head:
            return head
        node = head.next
        while node:
            print("node", node.val)
            n = head
            while(True):
                if n.next.val < node.val:
                    n = n.next
                else:
                    break
            new_node = node.next
            if node.val <= head.val:
                print(node.val)
                head = node
                node.next = n
            elif n.next.val == node.val:
                node.next = None
            else:
                node.next = n.next
                n.next = node
            node = new_node
        return head

if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(0)

    l5 = ListNode(0)
    l4 = ListNode(2, l5)
    l3 = ListNode(3, l4)
    l2 = ListNode(1, l3)
#    print(s.insertionSortList(l1))
    ans = s.insertionSortList(l2)
    while(ans):
        print (ans.val)
        ans = ans.next
        for i in range(100000):
            i + 1
