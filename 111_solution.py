"""
111. Climbing Stairs
中文
English

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Example

Example 1:
	Input:  n = 3
	Output: 3
	
	Explanation:
	1) 1, 1, 1
	2) 1, 2
	3) 2, 1
	total 3.


Example 2:
	Input:  n = 1
	Output: 1
	
	Explanation:  
	only 1 way.
"""

class Solution:
    def climbStairs(self, n):
        a = 0
        b = int(n != 0)
        for _ in range(n):
            a, b = b, a + b
        return b

