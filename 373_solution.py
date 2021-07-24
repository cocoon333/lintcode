"""
373. Partition Array by Odd and Even
中文
English

Partition an integers array into odd number first and even number second.
Example

Example 1:

Input: [1,2,3,4]
Output: [1,3,2,4]

Example 2:

Input: [1,4,2,3,5,6]
Output: [1,3,5,4,2,6]

Challenge

Do it in-place.
Notice

The answer is not unique. All you have to do is give a vaild answer.
"""

class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        start = 0
        end = len(nums) - 1
        while start < end:
            while nums[start] % 2 and start < end:
                start += 1
            while not nums[end] % 2 and end > start:
                end -= 1
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp

if __name__ == "__main__":
    s = Solution()
    l1 = [1, 2, 3, 4]
    l2 = [1, 4, 2, 3, 5, 6]
    s.partitionArray(l1)
    s.partitionArray(l2)
    print(l1)
    print(l2)
