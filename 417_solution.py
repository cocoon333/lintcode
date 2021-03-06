"""
417. Valid Number
中文
English

Validate if a given string is numeric.
Example

Example 1:

Input: "0"
Output: true
Explanation: "0" can be converted to 0

Example 2:

Input: "0.1"
Output: true
Explanation: "0.1" can be converted to 0.1

Example 3:

Input: "abc"
Output: false

Example 4:

Input: "1 a"
Output: false

Example 5:

Input: "2e10"
Output: true
Explanation: "2e10" represents 20,000,000,000

"""

class Solution:
    """
    @param s: the string that represents a number
    @return: whether the string is a valid number
    """
    def isNumber(self, s):
        try:
            s = s.strip('+')
            s = s.strip('-')
            s = s.strip('.')
            int(s)
            return True
        except:
            return False
