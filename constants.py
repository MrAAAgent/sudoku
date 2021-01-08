NUM_ROWS = 9
NUM_COLUMNS = 9
WIDTH = 600
HEIGHT = 650

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (96, 216, 232)
INCORRECT_RED = (255, 0, 0)
LOCKED_CELL_COLOUR = (189,189,189)
INCORRECT_CELL_COLOUR = (195,121,121)

TEST_BOARD = [
    [0,0,0,1,0,7,0,0,8],
    [8,0,7,4,0,0,0,2,0],
    [0,0,0,0,0,0,4,0,0],
    [4,3,0,6,0,5,0,0,0],
    [5,2,0,0,0,0,0,6,7],
    [0,0,0,2,0,9,0,1,4],
    [0,0,5,0,0,0,0,0,0],
    [0,8,0,0,0,2,7,0,6],
    [2,0,0,5,0,3,0,0,0]
]

BOARD_POSITION = (75,125)
CELL_SIZE = 50
BOARD_SIZE = CELL_SIZE*9

EASY = "1"
MEDIUM = "2"
HARD = "3"
EVIL = "4"

#ORIGINAL_FILLED_FONT
#SKETCH_FONT
#LOCKED_FONT

WINDOW_TITLE = "Sudoku - "
EASY_MODE_TITLE = "Easy"
MEDIUM_MODE_TITLE = "Medium"
HARD_MODE_TITLE = "Hard"
EVIL_MODE_TITLE = "Evil"
HIGHLIGHT_ERROR_TITLE = " (Training Mode)"
TRACK_ERROR_TITLE = " (Survival Mode)"

START_NEW_GAME_TITLE = "Start New Game"
START_NEW_GAME_MESSAGE = "You will lose all your progress on your current game. Are you sure you want to start a new game?"