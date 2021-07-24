'''
37. Reverse 3-digit Integer
English

Reverse a 3-digit integer.
Example

Example 1:

Input: number = 123
Output: 321

Example 2:

Input: number = 900
Output: 9

Notice

You may assume the given number is larger or equal to 100 but smaller than 1000.
'''

class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        n0 = number % 10
        n1 = (number % 100 - n0) // 10
        n2 = number // 100
        return n0 * 100 + n1 * 10 + n2


def regression():
    s = Solution()
    assert (s.reverseInteger(123) == 321)

if __name__ == '__main__':
    regression()
