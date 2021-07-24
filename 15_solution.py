"""
15. Permutations
中文
English

Given a list of numbers, return all possible permutations.
Example

Example 1:

Input: [1]
Output:
[
  [1]
]

Example 2:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Challenge

Do it without recursion.
Notice

You can assume that there is no duplicate numbers in the list.
"""
import copy

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        res = []
        self.helper(nums, res, [])
        return res

    def helper(self, nums, res, permutation):
        if len(permutation) == len(nums):
            res.append(copy.deepcopy(permutation))

        for i in range(len(nums)):
            if nums[i] not in permutation:
                permutation.append(nums[i])
                self.helper(nums, res, permutation)
                permutation.pop()

if __name__ == "__main__":
    s = Solution()
    print(s.permute([1]))
    print(s.permute([1, 2, 3]))
