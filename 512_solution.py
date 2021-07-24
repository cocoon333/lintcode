"""
512. Decode Ways
中文
English

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.
Example

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as AB (1 2) or L (12).

Example 2:

Input: "10"
Output: 1
"""

class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        if len(s) < 2:
            if s == "0" or not(s):
                return 0
            return 1
        res = [1, 1]
        for i in range(len(s)-1):
            segment = int(s[i:i+2])
            if 26 >= segment > 10 and s[i+1] != "0":
                res.append(res[i] + res[i+1])
            elif segment == 10 or segment == 20:
                res.append(res[i])
            elif s[i+1] != '0':
                res.append(res[i+1])
            else:
                return 0
        return res[len(s)]

if __name__ == "__main__":
    s = Solution()
    assert(s.numDecodings("12") == 2)
    assert(s.numDecodings("10") == 1)
    assert(s.numDecodings("19261001") == 0)
