"""
196. Missing Number
中文
English

Given an array contains N numbers of 0 .. N, find which number doesn't exist in the array.
Example

Example 1:

Input:[0,1,3]
Output:2

Example 2:

Input:[1,2,3]
Output:0

Challenge

Do it in-place with O(1) extra memory and O(n) time.
"""

class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def findMissing(self, nums):
        for i in range(len(nums)):
            if nums[i] != i:
                while nums[i] != i:
                    if nums[i] == len(nums):
                        nums[i] = -1
                        break
                    if nums[i] == -1:
                        break
                    temp = nums[i]
                    nums[i] = nums[temp]
                    nums[temp] = temp

        prev = nums[i]
        i = 0
        for j in range(len(nums)):
            if nums[j] == -1:
                continue
            if i != nums[j]:
                return i
            i += 1
        return i

if __name__ == "__main__":
    s = Solution()
    assert(s.findMissing([9,8,7,6,2,0,1,5,4]) == 3)
    assert(s.findMissing([0, 1, 3]) == 2)
    assert(s.findMissing([1, 2, 3]) == 0)
