# sudoku

This repository is my attempt at Sudoku written in Python using the Pygame library. It uses a backtracking algorithm to determine the solution to any Sudoku board that is retrieved using BeautifulSoup to parse through the HTML of a given difficulty puzzle (EASY, MEDIUM, HARD, EVIL) from https://www.websudoku.com.

It includes two different game modes: Training and Survival. Training is where all incorrect numbers will be highlighted for the player to see. Survival is where the player only has 3 lives where they will lose a life every incorrect number placed.

- To scribble in a number on a given cell without submitting, simply type the number.
- To submit a number, press ENTER/RETURN where you have the cell you want to submit is the selected square.
- To remove a scribble or submitted number, press BACKSPACE with the cell selected.

To run this locally, you will need to download this repository along with Python. It will also require the following libraries:
- pygame
- bs4
- requests

If you do not have these already installed on your computer, you can install any of them by typing the following command (given that you already have Python successfully installed) into command prompt:
pip install (INSERT NAME HERE)

Once you have everything set up, you can run the main.py file and enjoy playing Sudoku!
