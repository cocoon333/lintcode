"""
32. Minimum Window Substring
中文
English

Given two strings source and target. Return the minimum substring of source which contains each char of target.
Example

Example 1:

Input: source = "abc", target = "ac"
Output: "abc"

Example 2:

Input: source = "adobecodebanc", target = "abc"
Output: "banc"
Explanation: "banc" is the minimum substring of source string which contains each char of target "abc".

Example 3:

Input: source = "abc", target = "aa"
Output: ""
Explanation: No substring contains two 'a'.

Challenge

O(n) time
Notice

    If there is no answer, return "".
    You are guaranteed that the answer is unique.
    target may contain duplicate char, while the answer need to contain at least the same number of that char.
"""

from collections import Counter
class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        if len(source) < len(target):
            return ""
        t = Counter(target)
        s = Counter()
        start = 0
        minStart = 0
        minLength = 999999
        count = 0
        for i, char in enumerate(source):
            s.update(char)
            if char in t and s[char] <= t[char]:
                count += 1

            f_char = source[start]
            while f_char not in t or s[f_char] > t[f_char]:
                s[f_char] -= 1
                start += 1
                f_char = source[start]

            if count == len(target):
                if i - start + 1 < minLength:
                    minStart = start
                    minLength = i - start + 1
        if minLength == 999999:
            return ""
        return source[minStart:minStart+minLength]

if __name__ == "__main__":
    s = Solution()
#    assert(s.minWindow("abc", "ac") == "abc")
#    assert(s.minWindow("abc", "aa") == "")
    print(s.minWindow("absdfaabab", "adb"))
