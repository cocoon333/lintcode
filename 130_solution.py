"""
130. Heapify
中文
English

Given an integer array, heapify it into a min-heap array.
For a heap array A, A[0] is the root of heap, and for each A[i], A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].

Example

Example 1

Input : [3,2,1,4,5]
Output : [1,2,3,4,5]
Explanation : return any one of the legitimate heap arrays

Challenge

O(n) time complexity
Clarification

What is heap? What is heapify? What if there is a lot of solutions?

    Heap is a data structure, which usually have three methods: push, pop and top. where "push" add a new element the heap, "pop" delete the minimum/maximum element in the heap, "top" return the minimum/maximum element.
    Convert an unordered integer array into a heap array. If it is min-heap, for each element A[i], we will get A[i * 2 + 1] >= A[i] and A[i * 2 + 2] >= A[i].
    Return any of them.
"""

class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        for i in range(len(A)//2, -1, -1):
            self.moveUp(A, i, len(A)-1)
        

    def moveUp(self, aList, first, last):
        smallest = 2 * first + 1
        while smallest <= last:
            if smallest < last and aList[smallest] > aList[smallest+1]:
                smallest += 1

            if aList[smallest] < aList[first]:
                self.swap(aList, smallest, first)
                first = smallest
                smallest = 2 * first + 1
            else:
                return

    def swap(self, l, i, j):
        temp = l[i]
        l[i] = l[j]
        l[j] = temp

if __name__ == "__main__":
    s = Solution()
    l = [2, 3, 5, 7, 1]
    s.heapify(l)
    print(l)
