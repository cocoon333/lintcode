class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        if (not(A)):
            return 0
        lower = 0
        upper = len(A) - 1
        while (upper > lower):
            middle = (upper + lower)//2
            pivot = A[middle]
            if (target == pivot):
                return middle
            elif (target < pivot):
                upper = middle - 1
            else:
                lower = middle + 1
            print(lower)
            print(upper)
        closest = A[lower]
        if (closest < target):
            return lower + 1
        elif (closest == target):
            return lower
        else:
            if (lower == 0):
                return lower 
            return lower - 1

if (__name__ == "__main__"):
    s = Solution()
#    assert(s.searchInsert([1, 2, 3, 4, 5, 6], 3) == 2)
#    assert(s.searchInsert([1, 2, 3, 4, 5], 3) == 2)
#    assert(s.searchInsert([1, 2, 3, 4, 5], 5) == 4)
#
#    assert(s.searchInsert([1, 2, 3, 4, 5], 6) == 5)
#    assert(s.searchInsert([1, 2, 3, 4, 5], 0) == 0)
#    assert(s.searchInsert([1, 2, 3, 4, 5], 3) == 2)
#
#    assert(s.searchInsert([1], 2) == 1)
#    assert(s.searchInsert([], 5) == 0)
#    assert(s.searchInsert([1, 4, 5, 8, 11, 19, 23, 24], 15) == 5) 
#    print(s.searchInsert([6, 9, 14, 18, 23, 27], 17))
    print('answer', s.searchInsert([4, 6], 5))
