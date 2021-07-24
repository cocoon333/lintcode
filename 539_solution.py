"""
539. Move Zeroes
中文
English

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Example

Example 1:

Input: nums = [0, 1, 0, 3, 12],
Output: [1, 3, 12, 0, 0].

Example 2:

Input: nums = [0, 0, 0, 3, 1],
Output: [3, 1, 0, 0, 0].

Notice

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
"""
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        i = 0
        count = 0
        while i < len(nums):
            if i == len(nums) - count:
                return
            if not nums[i]:
                nums.append(nums.pop(i))
                count += 1
                continue
            i += 1

if __name__ == "__main__":
    s = Solution()
    l1 = [0, 1, 0, 3, 12]
    l2 = [0, 0, 0, 3, 1]
    s.moveZeroes(l1)
    s.moveZeroes(l2)
    assert(l1 == [1, 3, 12, 0, 0])
    assert(l2 == [3, 1, 0, 0, 0])
