"""
666. Guess Number Higher or Lower II
中文
English

We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.
However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.
Example

Example1

Input: 10
Output: 16
Explanation:
Given n = 10, I pick 2.
First round:  You guess 7, I tell you that it's lower. You pay $7.
Second round: You guess 3, I tell you that it's lower. You pay $3.
Third round:  You guess 1, I tell you that it's higher. You pay $1.
Game over. 1 is the number I picked.
You end up paying $7 + $3 + $1 = $11.

Given n = 10, I pick 4.
First round:  You guess 7, I tell you that it's lower. You pay $7.
Second round: You guess 3, I tell you that it's higher. You pay $3.
Third round:  You guess 5, I tell you that it's lower. You pay $5.
Game over. 4 is the number I picked.
You end up paying $7 + $3 + $5 = $15.

Given n = 10, I pick 8.
First round:  You guess 7, I tell you that it's higher. You pay $7.
Second round: You guess 9, I tell you that it's lower. You pay $9.
Game over. 8 is the number I picked.
You end up paying $7 + $7 + $9 = $16.

So given n = 10, the answer is 16.

Example2

Input: 5
Output: 6
"""

class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def getMoneyAmount(self, n):
        start = 1
        end = n
        res = 0
        while start < end:
            mid = (start + end) // 2
            guess = Guess.guess(mid)
            res += mid
            if not guess:
                return res
            elif guess == -1:
                end = mid - 1
            else:
                start = mid + 1
        return res
