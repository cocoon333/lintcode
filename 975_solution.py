"""
975. 2 Keys Keyboard
中文
English

Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

    Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
    Paste: You can paste the characters which are copied last time.
    Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example

Example 1:

Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

Example 2:

Input: 1
Output: 0

Notice

The n will be in the range [1, 1000].
"""

class Solution:
    """
    @param n: The number of 'A'
    @return: the minimum number of steps to get n 'A'
    """
    def minSteps(self, n):
        if n == 1:
            return 0
        max_factor = 1
        for i in range(2, int(n ** (0.5) + 1)):
            if not n % i:
                max_factor = i
        if max_factor == 1:
            return n
        return self.minSteps(max_factor) + self.minSteps(n // max_factor)

if __name__ == "__main__":
    s = Solution()
    assert(s.minSteps(3) == 3)
    assert(s.minSteps(1) == 0)
    assert(s.minSteps(5) == 5)
    assert(s.minSteps(25) == 10)
