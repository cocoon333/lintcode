"""
16. Permutations II
中文
English

Given a list of numbers with duplicate number in it. Find all unique permutations.
Example

Example 1:

Input: [1,1]
Output:
[
  [1,1]
]

Example 2:

Input: [1,2,2]
Output:
[
  [1,2,2],
  [2,1,2],
  [2,2,1]
]

Challenge

Using recursion to do it is acceptable. If you can do it without recursion, that would be great!
"""

import copy

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permuteUniqueDfs(self, nums):
        # write your code here
        nums.sort()
        res = []
        n = len(nums)
        self.dfs(nums,[],res,n)
        return res

    def dfs(self,nums,path,res,n):
        if len(path) == n:
            res.append(path)
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
            self.dfs(nums[:i]+nums[i+1:],path+[nums[i]],res,n)

    def permuteUnique(self, nums):
        res = []
        self.helper(nums, res, [], [])
        return res

    def helper(self, nums, res, permutation, indexes):
        if len(permutation) == len(nums):
            if permutation not in res:
                res.append(copy.deepcopy(permutation))

        for i in range(len(nums)):
            if i not in indexes:
                indexes.append(i)
                permutation.append(nums[i])
                self.helper(nums, res, permutation, indexes)
                permutation.pop()
                indexes.pop()

if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique([1, 1]))
    print(s.permuteUnique([1, 2, 2]))
    print(s.permuteUnique([-1,2,-1,2,1,-1,2,1]))
