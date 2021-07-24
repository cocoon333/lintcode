"""
159. Find Minimum in Rotated Sorted Array
中文
English

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.
Example

Example 1:

Input：[4, 5, 6, 7, 0, 1, 2]
Output：0
Explanation：
The minimum value in an array is 0.

Example 2:

Input：[2,1]
Output：1
Explanation：
The minimum value in an array is 1.

Notice

You can assume no duplicate exists in the array.
"""
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        start = 0
        end = len(nums) -1
        minimum = 999999
        while start < end:
            mid = (start + end) // 2
            if nums[mid] >= nums[end]:
                start = mid + 1
                if nums[start] < minimum:
                    minimum = nums[start]
            elif nums[mid] <= nums[end]:
                end = mid
                if nums[end] < minimum:
                    minimum = nums[end]
        return minimum

if __name__ == "__main__":
    s = Solution()
    print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
    print(s.findMin([2, 1]))
