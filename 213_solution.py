"""
213. String Compression
中文
English

Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3.

If the "compressed" string would not become smaller than the original string, your method should return the original string.

You can assume the string has only upper and lower case letters (a-z).
Example

Example 1:

Input: str = "aabcccccaaa"
Output: "a2b1c5a3"

Example 2:

Input: str = "aabbcc"
Output: "aabbcc"
"""

class Solution:
    """
    @param originalString: a string
    @return: a compressed string
    """
    def compress(self, originalString):
        count = 1
        i = 0
        l = [c for c in originalString]
        while i < len(l):
            if i > 0 and l[i] == l[i-1]:
                count += 1
                l.pop(i)
                continue
            elif i != 0:
                l.insert(i, str(count))
                count = 1
                i += 1
            i += 1

        ans = "".join(l) + str(count)
        if len(ans) < len(originalString):
            return ans
        else:
            return originalString

if __name__ == "__main__":
    s = Solution()
    assert(s.compress("aabcccccaaa") == "a2b1c5a3")
    assert(s.compress("aabbcc") == "aabbcc")
