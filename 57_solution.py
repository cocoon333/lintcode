"""
57. 3Sum
中文
English

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Example

Example 1:

Input:[2,7,11,15]
Output:[]

Example 2:

Input:[-1,0,1,2,-1,-4]
Output:	[[-1, 0, 1],[-1, -1, 2]]

Notice

Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

The solution set must not contain duplicate triplets.
"""

from collections import Counter
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        s = Counter(numbers)
        res = set()
        cache = set()
        for i, target in enumerate(numbers):
            for j, n1 in enumerate(numbers):
                if i != j:
                    if -(target+n1) in s:
                        if ((-(target+n1) == target or -(target+n1) == n1) and s[-(target+n1)] == 1) or (-(target+n1) == target == n1 and s[target] < 3):
                            continue
                        res.add(tuple(sorted([target, n1, -(target+n1)])))
        return list(map(sorted, res))

if __name__ == "__main__":
    s = Solution()
    assert(not s.threeSum([2, 7, 11, 15]))
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
