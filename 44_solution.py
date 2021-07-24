"""
44. Minimum Subarray
中文
English

Given an array of integers, find the continuous subarray with smallest sum.

Return the sum of the subarray.
Example

Example 1

Input：[1, -1, -2, 1]
Output：-3

Example 2

Input：[1, -1, -2, 1, -4]
Output：-6

Notice

The subarray should contain one integer at least.
"""

class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        temp = 0
        res = 99999
        for i in range(len(nums)):
            if temp < 0:
                temp += nums[i]
            else:
                temp = nums[i]

            if temp < res:
                res = temp
        return res

if __name__ == "__main__":
    s = Solution()
    assert(s.minSubArray([1, -1, -2, 1]) == -3)
    assert(s.minSubArray([1, -1, -2, 1, -4]) == -6)
