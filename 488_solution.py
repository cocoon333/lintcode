"""
488. Happy Number
中文
English

Write an algorithm to determine if a number is happy.

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
Example

Example 1:

Input:19
Output:true
Explanation:

19 is a happy number

    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1

Example 2:

Input:5
Output:false
Explanation:

5 is not a happy number

25->29->85->89->145->42->20->4->16->37->58->89
89 appears again.
"""
class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """
    def isHappy(self, n):
        current = n
        s = set()
        while True:
            m = map(int, str(current))
            current = sum([i**2 for i in m])
            if current == 1:
                return True
            elif current in s:
                return False
            s.add(current)

if __name__ == "__main__":
    s = Solution()
    assert(s.isHappy(19))
    assert(not s.isHappy(5))
    assert(s.isHappy(152395730))
