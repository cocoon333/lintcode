"""
408. Add Binary
中文
English

Given two binary strings, return their sum (also a binary string).
Example

Example 1:

Input:
a = "0", b = "0"
Output:
"0"

Example 2:

Input:
a = "11", b = "1"
Output:
"100"

"""

class Solution:
    """
    @param a: a number
    @param b: a number
    @return: the result
    """
    def addBinary(self, a, b):
        carry = 0
        added = min(len(a), len(b))
        res = ""
        for i in range(-1, -added-1, -1):
            temp = int(a[i]) + int(b[i]) + carry
            carry = 0
            if temp >= 2:
                carry = 1
                temp -= 2
            res = str(temp) + res


        if len(a) > added:
            if carry:
                return self.addBinary(a[0:len(a)-added]+"0"*added, str(carry) + res)
            return a[0:len(a)-added] + res
        elif len(b) > added:
            if carry:
                return self.addBinary(b[0:len(b)-added]+"0"*added, str(carry) + res)
            return b[0:len(b)-added] + res
        elif carry:
            res = str(carry) + res

        return res

if __name__ == "__main__":
    s = Solution()
    assert(s.addBinary("0", "0") == '0')
    assert(s.addBinary("11", "1") == '100')
    assert(s.addBinary("110", "10") == "1000")
    assert(s.addBinary("111", "1") == "1000")
    assert(s.addBinary("1", "111") == "1000")
