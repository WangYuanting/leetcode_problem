'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.


A sudoku puzzle...


...and its solution numbers marked in red.
'''


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """


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


#
class Solution1:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.board = board
        self.solve()

    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == ".":
                    return row, col
        return -1, -1

    def solve(self):
        row, col = self.findUnassigned()
        # no unassigned position is found, puzzle solved
        if row == -1 and col == -1:
            return True
        for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = "."
        return False

    def isSafe(self, row, col, ch):
        boxrow = row - row % 3
        boxcol = col - col % 3
        if self.checkrow(row, ch) and self.checkcol(col, ch) and self.checksquare(boxrow, boxcol, ch):
            return True
        return False

    def checkrow(self, row, ch):
        for col in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checkcol(self, col, ch):
        for row in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checksquare(self, row, col, ch):
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if self.board[r][c] == ch:
                    return False
        return True
#
class Solution2(object):
    def solveSudoku(self, board):
        self.board = board
        self.val = self.PossibleVals()
        self.Solver()

    def PossibleVals(self):
        nrows = len(self.board)
        ncols = len(self.board[0])
        digits = "123456789"
        val = {}
        d = {}
        for r in range(nrows):
            for c in range(ncols):
                if self.board[r][c] == ".":
                    val[(r, c)] = []
                else:
                    d[("r", r)] = d.get(("r", r), []) + [self.board[r][c]]
                    d[("c", c)] = d.get(("c", c), []) + [self.board[r][c]]
                    d[(r / 3, c / 3)] = d.get((r / 3, c / 3), []) + [self.board[r][c]]
        for k in val.keys():
            occupied = d.get((k[0] / 3, k[1] / 3), []) + d.get(("r", k[0]), []) + d.get(("c", k[1]), [])
            val[k] = [n for n in digits if n not in occupied]
        return val

    def Solver(self):
        if len(self.val) == 0:
            return True
        sKey = min(self.val.keys(), key=lambda key: len(self.val[key]))
        nums = self.val[sKey]
        for n in nums:
            update = {sKey: self.val[sKey]}
            if self.validOneCell(n, sKey, update):
                if self.Solver():
                    return True
            self.undo(sKey, update)
        return False

    def validOneCell(self, n, sKey, update):
        self.board[sKey[0]][sKey[1]] = n
        del self.val[sKey]
        (r, c) = sKey
        for k in self.val.keys():
            if n in self.val[k]:
                if r == k[0] or c == k[1] or (r / 3 == k[0] / 3 and c / 3 == k[1] / 3):
                    update[k] = n
                    self.val[k].remove(n)
                    if len(self.val[k]) == 0:
                        return False
        return True

    def undo(self, sKey, update):
        self.board[sKey[0]][sKey[1]] = "."
        for k in update.keys():
            if k not in self.val:
                self.val[k] = update[k]
            else:
                self.val[k].append(update[k])
#
a=Solution2()
b=a.solveSudoku([[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]])


