"""
834. Remove Duplicate Letters
中文
English

Given a string s which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
Example

Example1

Input: s = "bcabc"
Output: "abc"

Example2

Input: s = "cbacdcbc"
Output: "acdb"
"""

class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def removeDuplicateLetters(self, s):
        seen = set()
        res = ""
        for i in range(len(s)-1, -1, -1):
            if s[i] not in seen:
                seen.add(s[i])
                res = s[i] + res
            else:
                continue

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicateLetters("bcabc"))
    print(s.removeDuplicateLetters("cbacdcbc"))
