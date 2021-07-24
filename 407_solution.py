"""
407. Plus One
中文
English

Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
Example

Example 1:

Input: [1,2,3]
Output: [1,2,4]

Example 2:

Input: [9,9,9]
Output: [1,0,0,0]
"""
class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        return list(map(int, str(int(''.join(map(str, digits)))+1)))

