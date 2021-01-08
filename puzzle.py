import requests
from bs4 import BeautifulSoup
from constants import NUM_ROWS, NUM_COLUMNS, TEST_BOARD
from solve import solve_board

def get_puzzle(difficulty):
    try:
        websudoku_html = requests.get("https://nine.websudoku.com/?level={}".format(difficulty)).content
        soup = BeautifulSoup(websudoku_html, 'html.parser')
        puzzle_ids = []
        for r in range(NUM_ROWS):
            for c in range(NUM_COLUMNS):
                puzzle_ids.append("f{}{}".format(c,r))
        data = []
        for id in puzzle_ids:
            data.append(soup.find('input', id=id))
        board = [[0 for x in range(NUM_COLUMNS)] for x in range(NUM_ROWS)]
        for index, cell in enumerate(data):
            board[index//9][index%9] = int(cell['value'])
        return board
    except:
        return TEST_BOARD


def get_solution(board):
    solution = [[0 for x in range(NUM_COLUMNS)] for x in range(NUM_ROWS)]
    for r in range(NUM_ROWS):
        for c in range(NUM_COLUMNS):
            solution[r][c] = board[r][c]
    solve_board(solution)
    return solution