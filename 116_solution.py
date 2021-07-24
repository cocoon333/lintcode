"""
116. Jump Game
中文
English

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
Example

Example 1

Input : [2,3,1,1,4]
Output : true

Example 2

Input : [3,2,1,0,4]
Output : false

Notice

This problem have two method which is Greedy and Dynamic Programming.

The time complexity of Greedy method is O(n).

The time complexity of Dynamic Programming method is O(n^2).

We manually set the small data set to allow you pass the test in both ways. This is just to let you learn how to use this problem in dynamic programming ways. If you finish it in dynamic programming ways, you can try greedy method to make it accept again.
"""

class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        if len(A) < 2:
            return True
        max_jump = 0
        for i in range(len(A)):
            if A[i] == 0:
                if max_jump <= i < len(A)-1:
                    return False
            else:
                jump = i + A[i]
                if jump > max_jump:
                    max_jump = jump
        return True

if __name__ == "__main__":
    s = Solution()
    assert(s.canJump([2, 3, 1, 1, 4]))
    assert(s.canJump([2, 3, 1, 1, 0]))
    assert(s.canJump([0]))
    assert(not s.canJump([0, 3, 1, 1, 0]))
    assert(not s.canJump([3, 2, 1, 0, 4]))
