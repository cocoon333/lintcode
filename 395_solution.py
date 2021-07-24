"""
395. Coins in a Line II
中文
English

There are n coins with different value in a line. Two players take turns to take one or two coins from left side until there are no more coins left. The player who take the coins with the most value wins.

Could you please decide the first player will win or lose?

If the first player wins, return true, otherwise return false.
Example

Example 1:

Input: [1, 2, 2]
Output: true
Explanation: The first player takes 2 coins.

Example 2:

Input: [1, 2, 4]
Output: false
Explanation: Whether the first player takes 1 coin or 2, the second player will gain more value.
"""

class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        if len(values) < 3:
            return True
        dp = [0] * len(values)
        dp[-3] = values[-2] + values[-3]
        dp[-2] = values[-1] + values[-2]
        dp[-1] = values[-1]

        for i in range(-4, -len(values)-1, -1):
            if i == -4:
                dp[i] = values[i] + max(values[i+1], values[i+3])
            else:
                dp[i] = values[i] + max((min(dp[i+2], dp[i+3])), (values[i+1] + min(dp[i+3], dp[i+4])))

        if sum(values)-dp[0] < dp[0]:
            return True
        return False

if __name__ == "__main__":
    s = Solution()
    assert(s.firstWillWin([1, 2, 4, 8]))
    assert(s.firstWillWin([1, 2, 2]))
    assert(not s.firstWillWin([1, 2, 4]))
