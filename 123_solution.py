"""
123. Word Search
中文
English

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
Example

Example 1:

Input：["ABCE","SFCS","ADEE"]，"ABCCED"
Output：true
Explanation：
[    
     A B C E
     S F C S 
     A D E E
]
(0,0)A->(0,1)B->(0,2)C->(1,2)C->(2,2)E->(2,1)D

Example 2:

Input：["z"]，"z"
Output：true
Explanation：
[ z ]
(0,0)z
"""

class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, word, (i, j), set(), 0):
                    return True
        return False

    def helper(self, board, word, indexes, cache, char_i):
        if indexes in cache:
            return False
        i, j = indexes
        if word[char_i] != board[i][j]:
            return False
        cache.add(indexes)
        if char_i == len(word)-1:
            return True

        found = False

        c = set(cache)
        if i > 0:
#            print('up', char_i+1)
            found = self.helper(board, word, (i-1, j), cache, char_i+1)
            if not found:
                cache = c
        if i < len(board)-1 and not found:
#            print('down', char_i+1)
            found = found or self.helper(board, word, (i+1, j), cache, char_i+1)
            if not found:
                cache = c
        if j > 0 and not found:
#            print('left', char_i+1)
            c = cache
            found = self.helper(board, word, (i, j-1), cache, char_i+1)
            if not found:
                cache = c
        if j < len(board[0])-1 and not found:
#            print('right', char_i+1)
            c = cache
            found = self.helper(board, word, (i, j+1), cache, char_i+1)
            if not found:
                cache = c


        return found

if __name__ == "__main__":
    s = Solution()
    assert(s.exist(["ABCE",
                    "SFES",
                    "ADEE"], "ABCESEEEFS"))
    assert(s.exist(["abc","aed","afg"], 'abcdefg'))
    assert(not s.exist(['ABCE', 'SFCS', 'ADEE'], 'ABCB'))
    assert(not s.exist(['b', 'a', 'b', 'b', 'a'], "baa"))
    assert(s.exist(["ABCE","SFCS","ADEE"], "ABCCED"))
    assert(s.exist(["Z"], "Z"))
