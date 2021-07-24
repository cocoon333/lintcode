"""
149. Best Time to Buy and Sell Stock
中文
English

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Example

Example 1

Input: [3, 2, 3, 1, 2]
Output: 1
Explanation: You can buy at the third day and then sell it at the 4th day. The profit is 2 - 1 = 1

Example 2

Input: [1, 2, 3, 4, 5]
Output: 4
Explanation: You can buy at the 0th day and then sell it at the 4th day. The profit is 5 - 1 = 4

Example 3

Input: [5, 4, 3, 2, 1]
Output: 0
Explanation: You can do nothing and get nothing.
"""

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        for i in range(len(prices)-1):
            prices[i] = prices[i+1] - prices[i]
        prices = prices[:-1]

        max_profit = 0
        temp = 0
        for i in range(len(prices)):
            if temp < 0:
                temp = prices[i]
            else:
                temp += prices[i]
            if temp > max_profit:
                max_profit = temp
        
        return max_profit

if __name__ == "__main__":
    s = Solution()
    assert(s.maxProfit([3, 2, 3, 1, 2]) == 1)
    assert(s.maxProfit([1, 2, 3, 4, 5]) == 4)
    assert(s.maxProfit([5, 4, 3, 2, 1]) == 0)
