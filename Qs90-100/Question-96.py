'''
01/04/2024

Q: Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, 
but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called 
Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid 
in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical 
starting puzzle grid and its solution grid.

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be 
necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this).
The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because 
it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), 
contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions 
(the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; 
for example, 483 is the 3-digit number found in the top left corner of the solution grid above.

A: 24702

'''

# Create sudoku boards by creating lists of lists. Had to alter the final line of the final board (extra code at bottom).
sudoku = []

with open('sudoku.txt', 'r') as file:
    toAdd = []
    for line in file:
        if line[0] == 'G':
            sudoku.append(toAdd)
            toAdd = []
        else:
            toAdd.append(line[:-1])
    toAdd = toAdd[:-1]
    toAdd.append('000008006')
    sudoku.append(toAdd)
sudoku = sudoku[1:]


# Working with GPT, worked out the following functions. The backtrack is to account for 0 which cannot be solved initially.
def is_safe(board, row, col, num):
    # Check if 'num' is not already placed in current row, current column and current 3x3 box
    for x in range(9):
        if board[row][x] == num or board[x][col] == num or board[row - row % 3 + x // 3][col - col % 3 + x % 3] == num:
            return False
    return True

def solve_sudoku(board):
    empty_cell = find_empty_location(board)
    if not empty_cell:
        return True  # Puzzle solved

    row, col = empty_cell

    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Backtrack

    return False  # Triggers backtracking

def find_empty_location(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j
    return None


# Tota lis simply found by taking the first three numbers of the solved boards and adding them together. 
total = 0

for i in sudoku:
    # Convert the list of strings to a 2D list of integers
    sudoku_board = [[int(num) for num in row] for row in i]

    # Solve the Sudoku
    if solve_sudoku(sudoku_board):
        solved_sudoku = [''.join(map(str, row)) for row in sudoku_board]

    numb = ''
    solved_sudoku = solved_sudoku[0][0:3]
    for i in solved_sudoku:
        numb += i

    total += int(numb)

print(total)
