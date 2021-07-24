"""
144. Interleaving Positive and Negative Numbers
中文
English

Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.
Example

Example 1

Input : [-1, -2, -3, 4, 5, 6]
Outout : [-1, 5, -2, 4, -3, 6]
Explanation :  any other reasonable answer.

Challenge

Do it in-place and without extra memory.
Notice

You are not necessary to keep the original order of positive integers or negative integers.
"""
class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        mid = self.partition(A)
        start = 0
        if mid > len(A)//2:
            start = 1
        for i in range(start, len(A), 2):
            print(mid)
            self.swap(A, i, mid)
            mid += 1


    def partition(self, A):
        i = 0
        j = len(A) - 1
        while i < j:
            while A[i] < 0:
                i += 1
            while A[j] >= 0:
                j -= 1
            if i < j:
                self.swap(A, i, j)
        print(A)
        return i

    def swap(self, array, i, j):
        temp = array[i]
        array[i] = array[j]
        array[j] = temp

if __name__ == "__main__":
    s = Solution()
    l = [-1, -2, -3, 4, 5, 6]
    l1 = [-33,-19,30,26,21,-9]
    l2 = [-13,-8,-12,-15,-14,35,7,-1,11,27,10,-7,-12,28,18]
    s.rerange(l)
    s.rerange(l1)
    s.rerange(l2)

    print(l)
    print(l1)
    print(l2)
