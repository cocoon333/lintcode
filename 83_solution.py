"""
83. Single Number II
中文
English

Given 3*n + 1 non-negative integer, every numbers occurs triple times except one, find it.
Example

Example 1:

Input:  [1,1,2,3,3,3,2,2,4,1]
Output:  4

Example 2:

Input: [2,1,2,2]
Output:  1

Challenge

One-pass, constant extra space.
"""
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumberII(self, A):
        total = [0] * (len(bin(max(A))) - 2)
        for i in range(len(A)):
            s = bin(A[i])[2:]
            for j in range(len(s)):
                    total[j+len(total)-len(s)] += int(s[j])


        res = 0
        for j in range(len(total)):
            res += (total[j] % 3)* 2 ** (len(total) - j - 1)

        return res

if __name__ == "__main__":
    s = Solution()
    assert(s.singleNumberII([1,1,2,3,3,3,2,2,4,1]) == 4)
    assert(s.singleNumberII([2, 1, 2, 2]) == 1)
    assert(s.singleNumberII([43,16,45,89,45,45,2147483646,43,2147483647,89,89,2147483646,16,16,2147483646,43]) == 2147483647)
