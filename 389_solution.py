"""
389. Valid Sudoku
中文
English

Determine whether a Sudoku is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character ..
Example

Example 1:

Input:
["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]
Output: true
Explanation: 
The sudoku is look like this. It's vaild.

Valid Sudoku

Example 2:

Input:
["53..7j...","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]
Output: false
Explanation: 
The sudoku is look like this. It's invaild because there are two '5' in the first row and the sixth line.

image
Clarification

What is Sudoku?

    http://sudoku.com.au/TheRules.aspx
    https://en.wikipedia.org/wiki/Sudoku
    http://baike.baidu.com/subview/961/10842669.htm

Notice

A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""
from collections import Counter

class Solution:
    """
    @param board: the board
    @return: whether the Sudoku is valid
    """
    def isValidSudoku(self, board):
        for i in range(len(board)):
            c = Counter(board[i]).most_common(2)
            if c[-1][1] > 1 and len(c) > 1:
                print("double digit in row")
                return False

        for j in range(len(board[0])):
            l = []
            for i in range(len(board)):
                l.append(board[i][j])
            c = Counter(l).most_common(2)
            if c[-1][1] > 1 and len(c) > 1:
                print("double digit in column")
                return False

        for j in range(0, len(board), 3):
            for i in range(0, len(board), 3):
                l = []
                l.extend(board[i][j:j+3])
                l.extend(board[i+1][j:j+3])
                l.extend(board[i+2][j:j+3])
                c = Counter(l).most_common(2)
                if c[-1][1] > 1 and len(c) > 1:
                    print(l)
                    print("double digit in cube")
                    return False
        return True

if __name__ == "__main__":
    s = Solution()
    #print(s.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]))
    print(s.isValidSudoku(["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]))
