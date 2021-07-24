"""
138. Subarray Sum
中文
English

Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.
Example

Example 1:

Input:  [-3, 1, 2, -3, 4]
Output: [0, 2] or [1, 3].
Explanation: return anyone that the sum is 0.

Example 2:

Input:  [-3, 1, -4, 2, -3, 4]
Output: [1,5]	

Notice

There is at least one subarray that it's sum equals to zero.
"""

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        d = {}
        d[0] = -1
        sum_l = 0
        for i in range(len(nums)):
            sum_l += nums[i]
            if sum_l in d:
                return [d[sum_l]+1, i]
            d[sum_l] = i

if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([-3, 1, 2, -3, 4]))
    print(s.subarraySum([-3, 1, -4, 2, -3, 4]))
