"""
1348. Excel Sheet Column Number
中文
English

Given a column title as appear in an Excel sheet, return its corresponding column number.
Example

Example1

Input: "AB"
Output: 28

Example2

Input: "AC"
Output: 29

Notice

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
"""

class Solution:
    """
    @param s: a string
    @return: return a integer
    """
    def titleToNumber(self, s):
        offset = 64
        res = 0
        for i in range(len(s)):
            res += (ord(s[i])-offset) * 26 ** (len(s) - i - 1)
        return res

if __name__ == "__main__":
    s = Solution()
    assert(s.titleToNumber("AB") == 28)
    assert(s.titleToNumber("AC") == 29)
