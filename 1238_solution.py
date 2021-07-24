"""
1238. Find All Duplicates in an Array
中文
English

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.
Example

Example1

Input:
[4,3,2,7,8,2,3,1]
Output:
[2,3]

Example2

Input:
[10,2,5,10,9,1,1,4,3,7]
Output:
[1,10]

Challenge

Could you do it without extra space and in O(n) runtime?
"""
class Solution:
    """
    @param nums: a list of integers
    @return: return a list of integers
    """
    def findDuplicates(self, nums):
        res = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] >= 0:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
            else:
                res.append(abs(nums[i]))
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
