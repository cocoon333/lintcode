"""
659. Encode and Decode Strings
中文
English

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode
Example

Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
"""

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""
        for s in strs:
            res += s + " "
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        return str.split(' ')[:-1]

if __name__ == "__main__":
    s = Solution()
    assert(s.decode(s.encode(['a', 'b', 'c', 'd'])) == ['a', 'b', 'c', 'd'])
    assert(s.decode(s.encode([])) == [])
    assert(s.decode(s.encode(["lint","code","love","you"])) == ["lint","code","love","you"])
    assert(s.decode(s.encode(["we", "say", ":", "yes"])) == ["we", "say", ":", "yes"])
