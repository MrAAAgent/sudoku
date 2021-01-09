NUM_ROWS = 9
NUM_COLUMNS = 9
WIDTH = 600
HEIGHT = 650

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (96, 216, 232)
INCORRECT_RED = (255, 0, 0)
SKETCH_GRAY = (152, 144, 144)

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

WINDOW_TITLE = "Sudoku - "
EASY_MODE_TITLE = "Easy"
MEDIUM_MODE_TITLE = "Medium"
HARD_MODE_TITLE = "Hard"
EVIL_MODE_TITLE = "Evil"
HIGHLIGHT_ERROR_TITLE = " (Training Mode)"
TRACK_ERROR_TITLE = " (Survival Mode)"

START_NEW_GAME_TITLE = "Start New Game"
START_NEW_GAME_MESSAGE = "You will lose all your progress on your current game. Are you sure you want to start a new game?"
def START_NEW_GAME_SOLVED_MESSAGE(time):
    return "Congratulations on solving the puzzle in " + time + "! Start a new game?"
SOLVE_GAME_TITLE = "Solve Game"
SOLVE_GAME_MESSAGE = "Are you sure you want to give up? The board will complete itself."
TOGGLE_MODE_TITLE = "Change Game Mode"
TOGGLE_MODE_MESSAGE = "Are you sure you want to toggle to a different game mode? "
def TOGGLE_MODE_CUSTOM(highlight_incorrect_mode):
    if highlight_incorrect_mode:
        return "You will be entering Survival mode where you only have 3 lives."
    else:
        return "You will be entering Training mode where all incorrect cells are highlighted."
RESET_GAME_TITLE = "Reset Game"
RESET_GAME_MESSAGE = "Do you want to retry this puzzle? If NO, a new puzzle will be generated for you."

SKETCH_FONT = "couriernew"
SKETCH_SIZE = 30
ORIGINAL_FONT = "comicsans"
ORIGINAL_SIZE = 40
FILLED_FONT = "couriernew"
FILLED_SIZE = 40