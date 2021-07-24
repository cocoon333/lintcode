"""
151. Best Time to Buy and Sell Stock III
中文
English

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.
Example

Example 1

Input : [4,4,6,1,1,4,2,5]
Output : 6

Notice

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxProfit(self, nums):
        for i in range(len(nums)-1):
            nums[i] = nums[i+1] - nums[i]
        nums = nums[:-1]
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
        return max_sum + max(second_max, max_gain)

    def max_subarray(self, nums):
        start = 0
        max_start = 0
        end = 0
        max_sum = 0
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
    assert(s.maxProfit([2, 1]) == 0)
    assert(s.maxProfit([3, 2, 6, 5, 0, 3]) == 7)
    assert(s.maxProfit([4, 4, 6, 1, 1, 4, 2, 5]) == 6)
