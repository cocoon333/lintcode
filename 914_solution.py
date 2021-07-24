"""
914. Flip Game
中文
English

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.
Example

Example1

Input:  s = "++++"
Output: 
[
  "--++",
  "+--+",
  "++--"
]

Example2

Input: s = "---+++-+++-+"
Output: 
[
	"---+++-+---+",
	"---+++---+-+",
	"---+---+++-+",
	"-----+-+++-+"
]
"""

class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        res = []
        for i in range(len(s)-1):
            if s[i] == '+' == s[i+1]:
                res.append(s[:i] + "--" + s[i+2:])

        return res

if __name__ == "__main__":
    s = Solution()
    assert(s.generatePossibleNextMoves('++++') == ["--++", "+--+", "++--"])
    print(s.generatePossibleNextMoves('---+++-+++-+'))
