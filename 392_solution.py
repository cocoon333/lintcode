"""
392. House Robber
中文
English

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
Example

Example 1:

Input: [3, 8, 4]
Output: 8
Explanation: Just rob the second house.

Example 2:

Input: [5, 2, 1, 3]
Output: 8
Explanation: Rob the first and the last house.

Challenge

O(n) time and O(1) memory.
"""

class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        if len(A) < 2:
            return A[0]
        temp = max(A[0], A[1])
        even = A[0]
        odd = A[1]
        prev = -9999999
        for i in range(2, len(A)):
            if i % 2:
                odd = max(odd, prev) + A[i]
            else:
                even += max(even, prev) + A[i]

        return max(odd, even)

if __name__ == "__main__":
    s = Solution()
    assert(s.houseRobber([10, 1, 1, 10, 1, 1, 10]) == 30)
    assert(s.houseRobber([5, 2, 1, 3]) == 8)
    assert(s.houseRobber([3, 8, 4]) == 8)
