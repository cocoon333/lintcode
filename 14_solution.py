class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        if (nums):
            return self.binary_search(nums, target, 0, len(nums))
        return -1

    def binary_search(self, nums, target, left, right):
        if (right-left <= 1):
            if (nums[left] == target):
                return left
            else:
                return -1
        if (nums[(left+right)//2] > target):
            return self.binary_search(nums, target, left, (left+right)//2)
        else:
            return self.binary_search(nums, target, (left+right)//2, right)

if (__name__ == "__main__"):
    s = Solution()
    print(s.binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
    print(s.binarySearch([1, 2, 3], 4))
    print(s.binarySearch([], 4))
    print(s.binarySearch([1, 2, 3], 1))
    print(s.binarySearch([1, 2, 3], 3))
