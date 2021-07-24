"""
92. Backpack
中文
English

Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?
Example

Example 1:
	Input:  [3,4,8,5], backpack size=10
	Output:  9

Example 2:
	Input:  [2,3,5,7], backpack size=12
	Output:  12
	

Challenge

O(n x m) time and O(m) memory.

O(n x m) memory is also acceptable if you do not know how to optimize memory.
Notice

You can not divide any item into small pieces.
"""
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        if m == 0 or not A:
            return 0
        dp = [[0]*(len(A)+1) for i in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, len(A)+1):
                if i - A[j-1] >= 0:
                    dp[i][j] = max(dp[i][j-1], dp[i-A[j-1]][j-1] + A[j-1])
                else:
                    dp[i][j] = dp[i][j-1]

        return dp[-1][-1]

if __name__ == "__main__":
    s = Solution()
    assert(s.backPack(10, [3, 4, 8, 5]) == 9)
    assert(s.backPack(12, [2, 3, 5, 7]) == 12)
