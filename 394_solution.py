"""
394. Coins in a Line
中文
English

There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left. The player who take the last coin wins.

Could you please decide the first player will win or lose?

If the first player wins, return true, otherwise return false.
Example

Example 1:

Input: 1
Output: true

Example 2:

Input: 4
Output: true
Explanation:
The first player takes 1 coin at first. Then there are 3 coins left.
Whether the second player takes 1 coin or two, then the first player can take all coin(s) left.

Challenge

O(n) time and O(1) memory
"""

class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        if not n:
            return False
        prev_prev_win = True
        prev_win = True
        current_win = True
        for i in range(2, n):
            current_win = not(prev_prev_win and prev_win)
            prev_prev_win = prev_win
            prev_win = current_win

        return current_win

if __name__ == "__main__":
    s = Solution()
    assert(not s.firstWillWin(3))
    assert(s.firstWillWin(2))

    assert(s.firstWillWin(1))
    assert(s.firstWillWin(4))
