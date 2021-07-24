"""
47. Majority Element II
中文
English

Given an array of integers, the majority number is the number that occurs more than 1/3 of the size of the array.

Find it.
Example

Example 1:

Input: [99,2,99,2,99,3,3], 
Output: 99.

Example 2:

Input: [1, 2, 1, 2, 1, 3, 3], 
Output: 1.

Challenge

O(n) time and O(1) extra space.
Notice

There is only one majority number in the array.
"""

class Solution:
    """
    @param: nums: a list of integers
    @return: The majority number that occurs more than 1/3
    """
    def majorityNumber(self, nums):
        return max(nums, key=nums.count)

if __name__ == "__main__":
    s = Solution()
    assert(s.majorityNumber([99,2,99,2,99,3,3]) == 99)
    assert(s.majorityNumber([1, 2, 1, 2, 1, 3, 3]) == 1)
