"""
18. Subsets II
中文
English

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Example

Example 1:

Input: [0]
Output:
[
  [],
  [0]
]

Example 2:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

Challenge

Can you do it in both recursively and iteratively?
Notice

    Each element in a subset must be in non-descending order.
    The ordering between two subsets is free.
    The solution set must not contain duplicate subsets.
"""

from collections import Counter
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        c = Counter(nums)
        res = [[]]
        for n in sorted(c):
            for i in range(len(res)):
                for j in range(1, c[n]+1):
                    res.append(res[i] + [n]*j)
        return res

if __name__ == "__main__":
    s = Solution()
    assert(s.subsetsWithDup([0]) == [[], [0]])
    print(s.subsetsWithDup([1, 2, 2]))
