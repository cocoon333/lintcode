"""
17. Subsets
中文
English

Given a set of distinct integers, return all possible subsets.
Example

Example 1:

Input: [0]
Output:
[
  [],
  [0]
]

Example 2:

Input: [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

Challenge

Can you do it in both recursively and iteratively?
"""

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        res = []
        return self.helper(nums, res)

    def helper(self, nums, res):
        if len(nums) == 1:
            res.append(nums)
            return nums[0]
        temp = []
        temp.append(self.helper(nums[:len(nums)-1], res))
        temp.append(nums[-1])
        res.append(temp)
        return temp

if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1, 2, 3]))
