"""
517. Ugly Number
中文
English

Write a program to check whether a given number is an ugly number`.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
Example

Example 1:

Input: num = 8 
Output: true
Explanation:
8=2*2*2

Example 2:

Input: num = 14 
Output: false
Explanation:
14=2*7 

Notice

Note that 1 is typically treated as an ugly number.
"""
class Solution:
    """
    @param num: An integer
    @return: true if num is an ugly number or false
    """
    def isUgly(self, num):
        done = False
        while num > 1:
            if num % 2 == 0:
                num //= 2
            elif num % 3 == 0:
                num //= 3
            elif num % 5 == 0:
                num //= 5
            else:
                break
        if num == 1:
            return True
        return False

if __name__ == "__main__":
    s = Solution()
    assert(s.isUgly(8))
    assert(not s.isUgly(14))
