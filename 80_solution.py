class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    def median(self, nums):
        if (not(nums)):
            return 
        if (len(nums) % 2):
            return sorted(nums)[len(nums)//2]
        else:
            return sorted(nums)[(len(nums)//2)-1]
