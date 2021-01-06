from constants import NUM_ROWS, NUM_COLUMNS, TEST_BOARD

# assign a TEST_BOARD to board variable
# is a list of length 9 of lists of integers 0 through 9 of length 9
board = TEST_BOARD

# find an empty square on the board
# returns a tuple of (row, column) or None
def empty_square(board):
    for r in range(NUM_ROWS):
        for c in range(NUM_COLUMNS):
            if board[r][c] == 0:
                return (r, c)
    return None



# check if adding insert to the position onto the board is a valid move
# returns True if valid, False if not
def valid_add(board, insert, position):
    # check row
    for c in range(NUM_COLUMNS):
        if board[position[0]][c] == insert and position[1] != c:
            return False
    
    # check column
    for r in range(NUM_ROWS):
        if board[r][position[1]] == insert and position[0] != r:
            return False
    
    # check box
    # boxes labelled as such
    # (0,0) | (0, 1) | (0,2)
    # ++++++++++++++++++++++
    # (1,0) | (1, 1) | (1,2)
    # ++++++++++++++++++++++
    # (2,0) | (2, 1) | (2,2)
    box_x = position[1]//3 
    box_y = position[0]//3
    for r in range(box_y*3, box_y*3+3):
        for c in range(box_x*3, box_x*3+3):
            if (r,c) != position and board[r][c] == insert:
                return False
    
    return True



def solve_board(board):
    empty = empty_square(board)
    if not empty: # no more empty board spaces means that the board is solved under the backtracking algorithm
        return True
    else:
        for number in range(1,10):
            if valid_add(board, number, empty):
                board[empty[0]][empty[1]] = number

                if solve_board(board): # recursively call solve_board and if no solution exists by adding the current number
                    return True
                
                board[empty[0]][empty[1]] = 0 # then remove this number from the position



def print_board(board):
    for r in range(NUM_ROWS):
        if r%3 == 0 and r != 0:
            print("+ + + + + + + + + + + + + + +")

        for c in range(NUM_COLUMNS):
            if c%3 == 0 and c != 0:
                print("| ", end="")
            elif c == 8:
                print(board[r][c])
            else:
                print(board[r][c], " ", end="")
    print() # to print a newline at the end of a printing a board

#print_board(board)
#solve_board(board)
#print_board(board)