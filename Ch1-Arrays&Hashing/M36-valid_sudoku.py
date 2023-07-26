"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells 
need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain 
the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top 
left corner being modified to 8. Since there are two 8's in 
the top left 3x3 sub-box, it is invalid.
"""

"""
Thought process:

Naive/BF:
How about we iterate through the entire board and if it is a number,
we check the horiz, vert, and 3x3 square assoc with that number in the
sudoku board.
Time complexity: O(n^2)

Magic:
How can we use Naive to make it O(n)? Well what if instead of constantly
checking the row and col and square over and over, what if we store it the
value and its associated stuffs instead in multiple dicts, so we don't
have to check every square over and over.

Crux of the problem: the square itself. How can we break apart the squares
since there is no dividing line. Using floor division, we always get the
correct square. Also, breaking up the problem into different sections

"""
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    if ( board[row][col] in rows[row] or
                        board[row][col] in cols[col]  or
                        board[row][col] in squares[(row // 3, col//3)]
                    ):
                        return False
                    
                    cols[col].add(board[row][col])
                    rows[row].add(board[row][col])
                    squares[(row // 3, col//3)].add(board[row][col])
        
        return True