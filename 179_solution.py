"""
179. Update Bits

Given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to set all bits between i and j in N equal to M (e g , M becomes a substring of N start from i to j)
Example

Example 1:

Input: N=(10000000000)2 M=(10101)2 i=2 j=6
Output: N=(10001010100)2

Example 2:

Input: N=(10000000000)2 M=(11111)2 i=2 j=6
Output: N=(10001111100)2

Challenge

Minimum number of operations?
Clarification

You can assume that the bits j through i have enough space to fit all of M. That is, if M=10011， you can assume that there are at least 5 bits between j and i. You would not, for example, have j=3 and i=2, because M could not fully fit between bit 3 and bit 2.
Notice

In the function, the numbers N and M will given in decimal, you should also return a decimal number.
"""

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param i: A bit position
    @param j: A bit position
    @return: An integer
    """
    def updateBits(self, n, m, i, j):
        neg_n = False
        neg_m = False
        if n >= 0:
            bin_n = bin(n)[2:]
        else:
            bin_n = bin(n)[3:]
            neg_n = True
        if m >= 0:
            bin_m = bin(m)[2:]
        else:
            bin_m = bin(m)[3:]
            neg_m = True
        neg = neg_n ^ neg_m
        if neg:
            return -int(bin_n[:-j-1]+bin_m+bin_n[-i:], 2)
        return int(bin_n[:-j-1]+bin_m+bin_n[-i:], 2)

if __name__ == "__main__":
    s = Solution()
