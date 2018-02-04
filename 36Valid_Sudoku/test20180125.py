'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.


'''


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        nums=['1','2','3','4','5','6','7','8','9']


        for row in xrange(len(board)):
            temp_list=[]
            for col in xrange(len(board[row])):
                if board[row][col] in nums:
                    if board[row][col] in temp_list:
                        return False
                    else:
                        temp_list.append(board[row][col])
        for col in xrange(len(board)):
            temp_list=[]
            for row in xrange(len(board[col])):
                if board[row][col] in nums:
                    if board[row][col] in temp_list:
                        return False
                    else:
                        temp_list.append(board[row][col])
        for row in xrange(3):
            for col in xrange(3):
                temp_list = []
                for i in xrange(3):
                    for j in xrange(3):
                        if board[3*row+i][3*col+j] in nums:
                            if board[3*row+i][3*col+j] in temp_list:
                                return False
                            else:
                                temp_list.append(board[3*row+i][3*col+j])



        return True

def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        hash_table_row = {}
        hash_table_col = {}
        hash_table_block = {}
        m = len(board)
        n = len(board[0])

        for i in range(m):
            hash_table_row[i] = {}
            hash_table_col[i] = {}
            hash_table_block[i] = {}

        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    continue

                key = board[i][j]
                block = ((i / 3) * 3) + (j / 3)

                if key in hash_table_row[i] or key in hash_table_col[j] or key in hash_table_block[block]:
                    return False
                else:
                    hash_table_row[i][key] = True
                    hash_table_col[j][key] = True
                    hash_table_block[block][key] = True

        return True
