"""
423. Valid Parentheses
中文
English

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
Example

Example 1:

Input: "([)]"
Output: False

Example 2:

Input: "()[]{}"
Output: True

Challenge

Use O(n) time, n is the number of parentheses.
"""
class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        stack = []
        for char in s:
            if char == "(":
                stack.append(')')
            elif char == "[":
                stack.append(']')
            elif char == "{":
                stack.append('}')
            else:
                if len(stack) == 0 or stack.pop() != char:
                    return False
        if stack:
            return False
        return True
                


if __name__ == "__main__":
    s = Solution()
    assert(not s.isValidParentheses("([)]"))
    assert(s.isValidParentheses("()[]{}"))
    assert(not s.isValidParentheses("(("))
