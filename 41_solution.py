class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        return max_sub_array(nums, 0, len(nums)-1)

    def max_sub_array(self, nums, left, right):
        return max(max_sub_array(left, (left+right)//2), max_sub_array((left+right)//2, right), max_cross_middle(nums, left, right, (left+right)//2))

    def max_cross_middle(self, nums, left, right, middle):

