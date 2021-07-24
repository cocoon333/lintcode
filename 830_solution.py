"""
830. String Sort
中文
English

Given a string, sort the string with the first keyword which is the most commonly used characters and the second keyword which is the dictionary order.
Example

Example1

Input:  str = "bloomberg"
Output: "bbooeglmr"
Explanation:
'b' and 'o' appear the most frequently, but the dictionary sequence of 'b' is the smaller than 'o', so 'b' is ranked first, followed by 'o', and so on.

Example2

Input:  str = "lintcode"
Output: "cdeilnot"
Explanation:
All characters appear the same number of times, so directly in accordance with the dictionary order.

Notice

    The length of string is less than 10000.
    All characters are lowercase
"""

from collections import Counter
class Solution:
    """
    @param str: the string that needs to be sorted
    @return: sorted string
    """
    def stringSort(self, string):
        c = Counter(string)
        keys = list(c.keys())
        keys.sort()
        values = []
        res = ""

        for k in keys:
            values.append(c[k])

        while values:
            maximum = -1
            index = 0
            for i in range(len(values)):
                if maximum < values[i]:
                    maximum = values[i]
                    index = i
            res += keys[index] * values[index]
            keys.pop(index)
            values.pop(index)

        return res

if __name__ == "__main__":
    s = Solution()
    assert(s.stringSort("bloomberg") == "bbooeglmr")
    assert(s.stringSort("lintcode") == "cdeilnot")
