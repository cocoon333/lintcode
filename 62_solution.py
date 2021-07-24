"""
62. Search in Rotated Sorted Array
中文
English

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
Example

Example 1:

Input: [4, 5, 1, 2, 3] and target=1, 
Output: 2.

Example 2:

Input: [4, 5, 1, 2, 3] and target=0, 
Output: -1.

Challenge

O(logN) time
"""

class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        if not A:
            return -1
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end-start)//2
            if A[mid] == target:
                return mid
            elif A[start] < A[mid]:
                if A[start] <= target and target <= A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if A[mid] <= target and target <= A[end]:
                    start = mid
                else:
                    end = mid
        if A[start] == target:
            return start
        elif A[end] == target:
            return end
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.search([4, 3], 3))
    assert(s.search([4, 5, 1, 2, 3], 3) == 4)
    assert(s.search([5], 5) == 0)
    assert(s.search([4, 5, 1, 2, 3], 1) == 2)
    assert(s.search([4, 5, 1, 2, 3], 0) == -1)
    assert(s.search([], 0) == -1)
    assert(s.search([4, 5, 0, 1, 2, 3], 0) == 2)
    assert(s.search([1, 2, 3, 4, 5, 6], 4) == 3)
    assert(s.search([6, 5, 4, 3, 1, 2], 1) == 4)
