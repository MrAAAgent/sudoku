# define the original board
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def valid_add(board, num, position):
    for c in range(len(board[0])):
        if board[position[0]][c] == num and position[1] != c:
            return False


def print_board(board):
    for r in range(len(board)):
        if r%3 == 0 and r != 0:
            print("- - - - - - - - - - - - - - - -")

        for c in range(len(board[0])):
            if c%3 == 0 and c != 0:
                print("| ", end="")
            
            if c == 8:
                print(board[r][c])
            else:
                print(board[r][c], " ", end="")


def empty_square(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 0:
                return (r, c)
    return None

print_board(board)
#solve(board)
#print_board(board)
        