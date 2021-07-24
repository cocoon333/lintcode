"""
491. Palindrome Number
中文
English

Check a positive number is a palindrome or not.

A palindrome number is that if you reverse the whole number you will get exactly the same number.
Example

Example 1:

Input:11
Output:true

Example 2:

Input:1232
Output:false
Explanation:
1232!=2321

Notice

It's guaranteed the input number is a 32-bit integer, but after reversion, the number may exceed the 32-bit integer.
"""

class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """
    def isPalindrome(self, num):
        return str(num) == str(num)[::-1]

if __name__ == "__main__":
    s = Solution()
    assert(not s.isPalindrome(123))
    assert(not s.isPalindrome(12))
    assert(s.isPalindrome(1))
    assert(s.isPalindrome(100001))
    assert(s.isPalindrome(0))
