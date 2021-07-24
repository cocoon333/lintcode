"""
54. String to Integer (atoi)
中文
English

Implement function atoi to convert a string to an integer.

If no valid conversion could be performed, a zero value is returned.

If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
Example

Example 1

Input: "10"
Output: 10

Example 2

Input: "1"
Output: 1

Example 3

Input: "123123123123123"
Output: 2147483647
Explanation: 123123123123123 > INT_MAX, so we return INT_MAX

Example 4

Input: "1.0"
Output: 1
Explanation: We just need to change the first vaild number
"""

import re
class Solution:
    """
    @param str: A string
    @return: An integer
    """
    def atoi(self, str):
        res = ""
        found = False
        for i in range(len(str)):
            if re.search("[0-9]", str[i]):
                found = True
                res += str[i]
            elif found:
                break
            elif re.search("[+-]", str[i]):
                if re.search("[+-]", str[i+1]):
                    break
                res += str[i]
                found = True
        if res:
            res = int(res)
            if res > 2147483647:
                return 2147483647
            elif res < -2147483648:
                return -2147483648
            return res
        else:
            return 0

if __name__ == "__main__":
    s = Solution()
    print(s.atoi('10'))
    assert(s.atoi("10") == 10)
    assert(s.atoi("1") == 1)
    assert(s.atoi("1.0") == 1)
    assert(s.atoi(" 15+6") == 15)
