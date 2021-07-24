"""
670. Predict the Winner
中文
English

Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.
Example

Example1

Input: [1, 5, 2]
Output: false
Explanation:
Initially, player 1 can choose between 1 and 2. If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. Hence, player 1 will never be the winner and you need to return False.

Example2

Input: [1, 5, 233, 7]
Output: true
Explanation: 
Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233. Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

Notice

    1 <= length of the array <= 2000.
    Any scores in the given array are non-negative integers and will not exceed 10,000,000.
    If the scores of both players are equal, then player 1 is still the winner.
"""

class Solution:
    """
    @param nums: nums an array of scores
    @return: check if player 1 will win
    """
    def PredictTheWinner(self, nums):
        score_1 = 0
        score_2 = 0
        i = 0
        j = len(nums)-1
        turn = 0
        while i < j:
            score_difference_l = nums[i] - nums[i+1]
            score_difference_r = nums[j] - nums[j-1]
            if score_difference_l > score_difference_r:
                added_score = score_difference_l
                i += 1
            else:
                added_score = score_difference_r
                j -= 1
            if not turn % 2:
                score_1 += added_score
            else:
                score_2 += added_score
            turn += 1

        return score_1 >= score_2

if __name__ == "__main__":
    s = Solution()
    print(s.PredictTheWinner([1, 20, 4]))
    #assert(not s.PredictTheWinner([1, 5, 2]))
    #assert(s.PredictTheWinner([1, 5, 233, 2]))
