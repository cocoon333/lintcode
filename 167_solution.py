"""
167. Add Two Numbers
中文
English

You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
Example

Example 1:

Input: 7->1->6->null, 5->9->2->null
Output: 2->1->9->null	
Explanation: 617 + 295 = 912, 912 to list:  2->1->9->null

Example 2:

Input:  3->1->5->null, 5->9->2->null
Output: 8->0->8->null	
Explanation: 513 + 295 = 808, 808 to list: 8->0->8->null
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2
    """
    def addLists(self, l1, l2):
        n1 = l1
        n2 = l2
        r1 = []
        r2 = []
        while n1:
            r1.append(n1.val)
            n1 = n1.next
        while n2:
            r2.append(n2.val)
            n2 = n2.next
        r1.reverse()
        r2.reverse()
        r1 = int("".join(map(str, r1)))
        r2 = int("".join(map(str, r2)))
        res = list(map(int, str(r1 + r2)))
        head = ListNode(res[-1])
        node = head
        for i in range(len(res)-2, -1, -1):
            node.next = ListNode(res[i])
            node = node.next

        return head


if __name__ == "__main__":
    s = Solution()
    l3 = ListNode(5)
    l2 = ListNode(1, l3)
    l1 = ListNode(3, l2)

    l6 = ListNode(2)
    l5 = ListNode(9, l6)
    l4 = ListNode(5, l5)

    l8 = ListNode(9)
    l9 = ListNode(9, l8)

#    print(s.addLists(l1, l4).val)
    ans = s.addLists(l8, l9)
    while ans:
        print(ans.val)
        ans = ans.next
