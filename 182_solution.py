"""
182. Delete Digits

Given string A representing a positive integer which has N digits, remove any k digits of the number, the remaining digits are arranged according to the original order to become a new positive integer.

Find the smallest integer after remove k digits.

N <= 240 and k <= N,
Example

Example 1:

Input: A = "178542", k = 4
Output:"12"

Example 2:

Input: A = "568431", k = 3
Output:"431"
"""

class Solution:
    """
    @param A: A positive integer which has N digits, A is a string
    @param k: Remove k digits
    @return: A string
    """
    def DeleteDigits(self, A, k):
        A = list(A)
        count = 0
        while count < k:
            i = 0
            done = False
            while i < len(A) - 1:
                if A[i] > A[i+1]:
                    done = True
                    A.pop(i)
                    count += 1
                    if count > k:
                        return "".join(A).lstrip("0")
                    break
                else:
                    i += 1
            if done:
                continue
            if count < k:
                A.pop(i)
                count += 1

        return "".join(A).lstrip("0")

if __name__ == "__main__":
    s = Solution()
    assert(s.DeleteDigits("178542", 4) == "12")
    assert(s.DeleteDigits("568431", 3) == "431")
    assert(s.DeleteDigits("90249", 2) == "24")
    assert(s.DeleteDigits("10999", 2) == "99")
