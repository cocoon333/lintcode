"""
669. Coin Change
中文
English

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
Example

Example1

Input: 
[1, 2, 5]
11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example2

Input: 
[2]
3
Output: -1

Notice

You may assume that you have an infinite number of each kind of coin.
"""

class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        count = 0
        for i in range(len(coins)-1, -1, -1):
            coin = coins[i]
            while amount - coin >= 0:
                amount -= coin
                count += 1
            if amount == 0:
                return count
        if amount != 0:
            return -1
        else:
            return count

if __name__ == "__main__":
    s = Solution()
    assert(s.coinChange([1, 2, 5], 11) == 3)
    assert(s.coinChange([2], 3) == -1)
