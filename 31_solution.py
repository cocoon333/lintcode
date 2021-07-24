"""
31. Partition Array
中文
English

Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

    All elements < k are moved to the left
    All elements >= k are moved to the right

Return the partitioning index, i.e the first index i nums[i] >= k.
Example

Example 1:

Input:
[],9
Output:
0

Example 2:

Input:
[3,2,2,1],2
Output:1
Explanation:
the real array is[1,2,2,3].So return 1

Challenge

Can you partition the array in-place and in O(n)?
Notice

You should do really partition in array nums instead of just counting the numbers of integers smaller than k.

If all elements in nums are smaller than k, then return nums.length
"""
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        start = 0
        end = len(nums)-1
        while start < end:
            while nums[start] < k and start < end:
                start += 1
            while nums[end] >= k and end >= start:
                end -= 1
            if start == end:
                break
            else:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
        if end >= 0 and nums[end] < k:
            start += 1
        return start

if __name__ == "__main__":
    s = Solution()
    assert(s.partitionArray([7,7,9,8,6,6,8,7,9,8,6,6], 10) == 12)
    assert(s.partitionArray([3,2,2,1],2) == 1)
    assert(s.partitionArray([],9) == 0)
