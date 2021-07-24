"""
171. Anagrams
中文
English

Given an array of strings, return all groups of strings that are anagrams.
Example

Example 1:

Input:["lint", "intl", "inlt", "code"]
Output:["lint", "inlt", "intl"]

Example 2:

Input:["ab", "ba", "cd", "dc", "e"]
Output: ["ab", "ba", "cd", "dc"]

Challenge

What is Anagram?

    Two strings are anagram if they can be the same after change the order of characters.

Notice

All inputs will be in lower-case
"""
class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        cache = {}
        res = []
        for string in strs:
            k = tuple(sorted(string))
            if k in cache:
                if type(cache[k]) == bool:
                    res.append(string)
                else:
                    res.append(cache[k])
                    cache[k] = False
                    res.append(string)
            else:
                cache[k] = string
        return res

if __name__ == "__main__":
    s = Solution()
    assert(s.anagrams(["", ""]) == ["", ""])
    assert(s.anagrams(['lint', 'intl', 'inlt', 'code']) == ['lint', 'intl', 'inlt'])
    assert(s.anagrams(["ab", "ba", "cd", "dc", "e"]) == ["ab", "ba", "cd", "dc"])
