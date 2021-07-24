import re
"""
49. Sort Letters by Case
中文
English

Given a string which contains only letters. Sort it by lower case first and upper case second.
Example

Example 1:
	Input:  "abAcD"
	Output:  "acbAD"

Example 2:
	Input: "ABC"
	Output:  "ABC"
	

Challenge

Do it in one-pass and in-place.
Notice

It's NOT necessary to keep the original order of lower-case letters and upper case letters.
"""

class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        if not chars:
            return
        i = 0
        j = len(chars)-1
        while True:
            while re.search('[a-z]', chars[i]) and i < len(chars):
                i += 1
            while re.search('[A-Z]', chars[j]) and j >= 0:
                j -= 1
            if i >= j:
                return

            temp = chars[i]
            chars[i] = chars[j]
            chars[j] = temp

if __name__ == "__main__":
    s = Solution()
    l = ['a', 'b', 'A', 'c', 'D']
    s.sortLetters(l)
    print (l)
