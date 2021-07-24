"""
1016. Minimum Swaps To Make Sequences Increasing
中文
English

We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i]. Note that both elements are in the same index position in their respective sequences.

After some number of swaps, A and B are both strictly increasing. (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing. It is guaranteed that the given input always makes it possible.
Example

Example 1:

Input: A = [1,3,5,4], B = [1,2,3,7]
Output: 1
Explanation: Swap A[3] and B[3]. Then the sequences are:
  A = [1,3,5,7] and B = [1,2,3,4],
  which are both strictly increasing.

Example 2:

Input: A = [2,4,5,7,10], B = [1,3,4,5,9]
Output: 0

Notice

    A, B are arrays with the same length, and that length will be in the range of [1, 1000].
    A[i], B[i] are integer values in the range of [0, 2000].
"""

class Solution:
    """
    @param A: an array
    @param B: an array
    @return: the minimum number of swaps to make both sequences strictly increasing
    """
    def minSwap(self, A, B):
        a = len(A)
        swap = 1
        no_swap = 0

        for i in range(1, len(A)):
            new_swap = a
            new_no_swap = a
            if A[i] > A[i-1] and B[i] > B[i-1]:
                new_no_swap = no_swap
                new_swap = swap + 1
            if B[i] > A[i-1] and A[i] > B[i-1]:
                new_no_swap = min(new_no_swap, swap)
                new_swap = min(new_swap, no_swap+1)
            swap = new_swap
            no_swap = new_no_swap
        return min(swap, no_swap)
    
if __name__ == "__main__":
    s = Solution()
    assert(s.minSwap([0,7,8,10,10,11,12,  13  ,19,18], [4,4,5,7,11,14,15, 16  ,17,20]) == 4)
    assert(s.minSwap([1,4,5,6,7,8,9,11,12,13,15,17,18,25,26,26,29,30,34,35,35,39,40,41,42,47,48,49,50,51,54,60,59,63,63,64,65,67,68,70,72,75,76,77,79,90,82,83,85,101,90,92,98,99,101,102,104,105,107,109,111,115,117,119,120,125,126,128,131,132,134,138,141,143,147,148,150,151,153,154,157,159,164,165,167,171,174,175,178,179,183,184,187,188,189,192,194,195,197,200], [3,4,5,6,10,14,16,17,18,19,20,21,22,23,24,28,28,29,33,34,38,41,43,46,48,49,50,52,53,54,57,56,61,62,64,67,70,71,73,75,76,80,81,86,87,80,91,97,100,88,103,104,107,110,111,113,116,118,123,124,129,132,133,134,136,139,140,141,142,143,144,145,146,147,148,149,150,151,153,154,155,163,165,170,172,174,175,176,176,182,184,185,187,188,191,190,194,195,198,199]) == 8)
    assert(s.minSwap([3,5,6,9,14,15,15,18,17,20], [3,4,5,8,10,14,17,16,19,19]) == 2)
    assert(s.minSwap([2, 4, 5, 7, 10], [1, 3, 4, 5, 9]) == 0)
    assert(s.minSwap([1, 3, 5, 4], [1, 2, 3, 7]) == 1)
