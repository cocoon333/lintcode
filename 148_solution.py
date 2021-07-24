"""
148. Sort Colors
中文
English

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Example

Example 1

Input : [1, 0, 1, 2]
Output : [0, 1, 1, 2]
Explanation : sort it in-place

Challenge

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
Notice

You are not suppose to use the library's sort function for this problem.
You should do it in-place (sort numbers in the original array).
"""

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):
        zeros = 0
        ones = 0
        twos = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            elif nums[i] == 1:
                ones += 1
            else:
                twos += 1

        for i in range(len(nums)):
            if i < zeros:
                nums[i] = 0
            elif i < zeros + ones:
                nums[i] = 1
            else:
                nums[i] = 2

if __name__ == "__main__":
    s = Solution()
    l = [1, 0, 1, 2]
    s.sortColors(l)
    print(l)
