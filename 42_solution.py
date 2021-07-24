"""
42. Maximum Subarray II
中文
English

Given an array of integers, find two non-overlapping subarrays which have the largest sum.
The number in each subarray should be contiguous.
Return the largest sum.
Example

Example 1:

Input:
[1, 3, -1, 2, -1, 2]
Output:
7
Explanation:
the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2].

Example 2:

Input:
[5,4]
Output:
9
Explanation:
the two subarrays are [5] and [4].

Challenge

Can you do it in time complexity O(n) ?
Notice

The subarray should contain at least one number
"""

class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        if len(nums) < 3:
            return sum(nums)
        max_sum, start, end = self.max_subarray(nums)

        max_gain = 0
        temp = 0
        for i in range(start+1, end):
            if temp > 0:
                temp -= nums[i]
            else:
                temp = -nums[i]
            if temp > max_gain:
                max_gain = temp
        second_max = self.max_subarray(nums[:start] + nums[end+1:])[0]
        if not max_gain and start == end:
            return max_sum + second_max
        return max_sum + max(second_max, max_gain)

    def max_subarray(self, nums):
        start = 0
        max_start = 0
        end = 0
        max_sum = -99999
        temp = 0
        for i in range(len(nums)):
            if temp < 0:
                start = i
                temp = nums[i]
            else:
                temp += nums[i]

            if temp > max_sum:
                max_sum = temp
                end = i
                max_start = start

        if temp > max_sum:
            max_sum = temp
            end = len(nums)-1
            max_start = start
        return (max_sum, max_start, end)

if __name__ == "__main__":
    s = Solution()
    assert(s.maxTwoSubArrays([-1, -2, -3, -100, -1, -50]) == -2)
    assert(s.maxTwoSubArrays([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-2,1,-15,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == 44)
    assert(s.max_subarray([-10, 4]) == (4, 1, 1))
    assert(s.maxTwoSubArrays([5, -10, 4]) == 9)
    assert(s.max_subarray([5, -10, 4]) == (5, 0, 0))
    assert(s.maxTwoSubArrays([1, 3, -1, 2, -1, 2]) == 7)
    assert(s.maxTwoSubArrays([5, 4]) == 9)
    assert(s.maxTwoSubArrays([0, -1]) == -1)
