"""
424. Evaluate Reverse Polish Notation
中文
English

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.
Example

Example 1:

Input: ["2", "1", "+", "3", "*"] 
Output: 9
Explanation: ["2", "1", "+", "3", "*"] -> (2 + 1) * 3 -> 9

Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: ["4", "13", "5", "/", "+"] -> 4 + 13 / 5 -> 6
"""

class Solution:
    """
    @param tokens: The Reverse Polish Notation
    @return: the value
    """
    def evalRPN(self, tokens):
        i = 0
        while i < len(tokens):
            if tokens[i] == "+":
                tokens[i] = tokens[i-2] + tokens[i-1]
                tokens.pop(i-1)
                tokens.pop(i-2)
                i -= 2
            elif tokens[i] == "-":
                tokens[i] = tokens[i-2] - tokens[i-1]
                tokens.pop(i-1)
                tokens.pop(i-2)
                i -= 2
            elif tokens[i] == "*":
                tokens[i] = tokens[i-2] * tokens[i-1]
                tokens.pop(i-1)
                tokens.pop(i-2)
                i -= 2
            elif tokens[i] == "/":
                tokens[i] = int(tokens[i-2] / tokens[i-1])
                tokens.pop(i-1)
                tokens.pop(i-2)
                i -= 2
            elif type(tokens[i]) == str:
                tokens[i] = int(tokens[i])
            i += 1

        return tokens[0]

if __name__ == "__main__":
    s = Solution()
    assert(s.evalRPN(["2", "1", "+", "3", "*"]) == 9)
    assert(s.evalRPN(["4", "13", "5", "/", "+"]) == 6)
    assert(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22)
