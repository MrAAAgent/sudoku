import pygame
from button import *
from solve import solve_board
from puzzle import *
from constants import *
import tkinter as tkinter
from tkinter import messagebox
import time
pygame.font.init()
pygame.mixer.init()

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = False
        self.board = []
        self.solution = []
        self.difficulty = None
        self.original_filled = []
        self.sketch_filled = []
        self.entered_filled = []
        self.strikes = None
        self.selected_square = None
        self.mouse_position = None
        self.original_font = pygame.font.SysFont(ORIGINAL_FONT, ORIGINAL_SIZE)
        self.sketch_font = pygame.font.SysFont(SKETCH_FONT, SKETCH_SIZE)
        self.filled_font = pygame.font.SysFont(FILLED_FONT, FILLED_SIZE)
        self.start_time = 0
        self.play_time = 0
        self.buttons = []
        self.highlight_incorrect_mode = True
        self.incorrect_tracker = False
        self.incorrect_submissions = []
        self.solved = False
        self.solved_prompt = False
        self.set_board(EASY)
        
    def start_game(self):                
        self.startup()
        self.running = True
        while self.running:
            if self.start_time:
                self.handle_events()
                self.update_state()
                self.draw()  
                self.play_time = round(time.time() - self.start_time)
        pygame.quit()    

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.selected_square = self.board_position()
                if not self.selected_square or self.selected_square in self.original_filled:
                    self.selected_square = None
                
                for button in self.buttons:
                    if button.hovered:
                        root = tkinter.Tk()
                        root.withdraw() # hide the tkinter root window
                        if button.text == "Toggle Mode":
                            confirmation = tkinter.messagebox.askquestion(button.confirmation_title, button.confirmation_message + TOGGLE_MODE_CUSTOM(self.highlight_incorrect_mode))
                        elif not self.solved:
                            confirmation = tkinter.messagebox.askquestion(button.confirmation_title, button.confirmation_message)
                        else:
                            confirmation = 'yes'
                        if confirmation == 'yes':
                            button.click()

            if event.type == pygame.KEYDOWN and self.selected_square != None:
                try:
                    int(event.unicode)
                    if int(event.unicode) > 0:
                        if self.selected_square not in self.entered_filled:
                            self.board[self.selected_square[1]][self.selected_square[0]] = int(event.unicode)
                            if self.selected_square not in self.sketch_filled:
                                self.sketch_filled.append(self.selected_square) 
                except:
                    if event.key == pygame.K_BACKSPACE:
                        self.board[self.selected_square[1]][self.selected_square[0]] = 0
                        if self.selected_square in self.sketch_filled:
                            self.sketch_filled.remove(self.selected_square)
                        elif self.selected_square in self.entered_filled:
                            self.entered_filled.remove(self.selected_square)
                    elif event.key == pygame.K_RETURN:
                        if self.selected_square in self.sketch_filled:
                            self.sketch_filled.remove(self.selected_square)
                            self.entered_filled.append(self.selected_square)
                    elif event.key == pygame.K_LEFT:
                        if self.selected_square[0] > 0 and ((self.selected_square[0]-1, self.selected_square[1]) not in self.original_filled):
                            self.selected_square = (self.selected_square[0]-1, self.selected_square[1])
                    elif event.key == pygame.K_RIGHT:
                        if self.selected_square[0] < NUM_ROWS-1 and ((self.selected_square[0]+1, self.selected_square[1]) not in self.original_filled):
                            self.selected_square = (self.selected_square[0]+1, self.selected_square[1])
                    elif event.key == pygame.K_UP:
                        if self.selected_square[1] > 0 and ((self.selected_square[0], self.selected_square[1]-1) not in self.original_filled):
                            self.selected_square = (self.selected_square[0], self.selected_square[1]-1)
                    elif event.key == pygame.K_DOWN:
                        if self.selected_square[1] < NUM_COLUMNS-1 and ((self.selected_square[0], self.selected_square[1]+1) not in self.original_filled):
                            self.selected_square = (self.selected_square[0], self.selected_square[1]+1)

    def board_position(self):
        if self.mouse_position[0] < BOARD_POSITION[0] or self.mouse_position[0] > BOARD_POSITION[0]+BOARD_SIZE:
            return False
        elif self.mouse_position[1] < BOARD_POSITION[1] or self.mouse_position[1] > BOARD_POSITION[1]+BOARD_SIZE:
            return False
        return ((self.mouse_position[0]-BOARD_POSITION[0])//CELL_SIZE, (self.mouse_position[1]-BOARD_POSITION[1])//CELL_SIZE)

    def update_state(self):
        self.mouse_position = pygame.mouse.get_pos()
        for button in self.buttons:
            button.update_button_state(self.mouse_position)

        self.check_for_incorrect()
        self.check_solved()

    def check_for_incorrect(self):
        self.incorrect_submissions = []
        for r in range(NUM_ROWS):
            for c in range(NUM_COLUMNS):
                if self.board[r][c] != 0 and self.board[r][c] != self.solution[r][c] and (c,r) in self.entered_filled:
                    if self.incorrect_tracker:
                        self.strikes += 1
                        self.entered_filled.remove((c,r))
                        self.board[r][c] = 0
                    self.incorrect_submissions.append((c, r))


    def check_solved(self):
        if self.board == self.solution and not len(self.sketch_filled) and not self.solved:
            self.solved = True
            self.solved_prompt = True

    def draw(self):
        self.window.fill(WHITE)

        for button in self.buttons:
            button.draw_button(self.window)

        self.draw_time(self.window)
        if self.incorrect_tracker:
            self.draw_strikes(self.window)        

        if self.selected_square:
            self.draw_selected(self.window, self.selected_square)
        
        self.draw_incorrect(self.window)
        self.draw_board(self.window)
        self.draw_board_numbers(self.window)

        pygame.display.update()
        
        if self.strikes == 3:
            root = tkinter.Tk()
            root.withdraw() # hide the tkinter root window
            confirmation = tkinter.messagebox.askquestion(RESET_GAME_TITLE, RESET_GAME_MESSAGE)
            if confirmation == 'yes':
                self.reset_board()
            else:
                self.set_board(self.difficulty)
        
        if self.solved_prompt:
            root = tkinter.Tk()
            root.withdraw() # hide the tkinter root window
            confirmation = tkinter.messagebox.askquestion(START_NEW_GAME_TITLE, START_NEW_GAME_SOLVED_MESSAGE(self.format_time()))
            if confirmation == 'yes':
                self.set_board(self.difficulty)
            else:
                self.solved_prompt = False
        
            


    def draw_board(self, window):
        pygame.draw.rect(window, BLACK, (BOARD_POSITION[0], BOARD_POSITION[1], WIDTH-150, HEIGHT-200), 2)
        for c in range(9):
            if c%3 != 0:
                pygame.draw.line(window, BLACK, (BOARD_POSITION[0]+c*CELL_SIZE, BOARD_POSITION[1]), (BOARD_POSITION[0]+c*CELL_SIZE, BOARD_POSITION[1]+450))
                pygame.draw.line(window, BLACK, (BOARD_POSITION[0], BOARD_POSITION[1]+c*CELL_SIZE), (BOARD_POSITION[0]+450, BOARD_POSITION[1]+c*CELL_SIZE))
            else:
                pygame.draw.line(window, BLACK, (BOARD_POSITION[0]+c*CELL_SIZE, BOARD_POSITION[1]), (BOARD_POSITION[0]+c*CELL_SIZE, BOARD_POSITION[1]+450), 2)
                pygame.draw.line(window, BLACK, (BOARD_POSITION[0], BOARD_POSITION[1]+c*CELL_SIZE), (BOARD_POSITION[0]+450, BOARD_POSITION[1]+c*CELL_SIZE), 2)


    def draw_board_numbers(self, window):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLUMNS):
                if self.board[r][c] != 0:
                    position = (c*CELL_SIZE+BOARD_POSITION[0], r*CELL_SIZE+BOARD_POSITION[1])
                    self.draw_number(window, str(self.board[r][c]), (c,r), position)

    def draw_selected(self, window, position):
        pygame.draw.rect(window, LIGHT_BLUE, (position[0]*CELL_SIZE+BOARD_POSITION[0], position[1]*CELL_SIZE+BOARD_POSITION[1], CELL_SIZE, CELL_SIZE))

    
    def draw_incorrect(self, window):
        for position in self.incorrect_submissions:
            pygame.draw.rect(window, INCORRECT_RED, (position[0]*CELL_SIZE+BOARD_POSITION[0], position[1]*CELL_SIZE+BOARD_POSITION[1], CELL_SIZE, CELL_SIZE))
    

    def load_buttons(self):
        self.buttons.append(Button(20, 40, WIDTH//7, 40,
            confirmation_title=SOLVE_GAME_TITLE, confirmation_message=SOLVE_GAME_MESSAGE,
            function=self.solve, colour=(27,142,207), text="Solve"))
        self.buttons.append(Button(140, 40, WIDTH//7, 40, colour=(117,172,112),
            function=self.set_board, params=EASY, text="Easy"))
        self.buttons.append(Button(WIDTH//2-(WIDTH//7)//2, 40, WIDTH//7, 40, colour=(204,197,110),
            function=self.set_board, params=MEDIUM, text="Medium"))
        self.buttons.append(Button(380, 40, WIDTH//7, 40, colour=(199,129,48),
            function=self.set_board, params=HARD, text="Hard"))
        self.buttons.append(Button(500, 40, WIDTH//7, 40, colour=(207,68,68),
            function=self.set_board, params=EVIL, text="Evil"))
        self.buttons.append(Button(465, 590, WIDTH//5, 40,
            confirmation_title=TOGGLE_MODE_TITLE, confirmation_message=TOGGLE_MODE_MESSAGE,
            function=self.toggle_mode, colour=(27,142,207), text="Toggle Mode"))

    def draw_number(self, window, number, cell, position):
        if  cell in self.sketch_filled:
            printed_number = self.sketch_font.render(number, False, SKETCH_GRAY)
            adjusted_position = (position[0]+5, position[1])
        elif cell in self.entered_filled:
            printed_number = self.filled_font.render(number, False, BLACK)
            adjusted_position = (position[0] + (CELL_SIZE - printed_number.get_width())//2, position[1] + (CELL_SIZE - printed_number.get_height())//2)
        else:
            printed_number = self.original_font.render(number, False, BLACK)
            adjusted_position = (position[0] + (CELL_SIZE - printed_number.get_width())//2, position[1] + (CELL_SIZE - printed_number.get_height())//2)
        window.blit(printed_number, adjusted_position)


    def startup(self):
        self.load_buttons()
        # music is from DooPiano: TWICE [Be as ONE] Piano Cover
        pygame.mixer.music.load("sudoku_background_music.mp3")
        pygame.mixer.music.play(-1,0.0)
        pygame.mixer.music.set_volume(0.1)

    def set_board(self, difficulty=""):
        if difficulty:
            self.board = get_puzzle(difficulty)
            self.solution = get_solution(self.board)
            self.difficulty = difficulty
            self.original_filled = []
            for r in range(NUM_ROWS):
                for c in range(NUM_COLUMNS):
                    if self.board[r][c] != 0:
                        self.original_filled.append((c, r))
            self.sketch_filled = []
            self.entered_filled = []
            self.strikes = 0
            self.solved = False
            self.solved_prompt = 0
            self.start_time = time.time()
            self.set_window_title()


    def solve(self):
        if not self.solved:
            for entered in self.entered_filled:
                if self.board[entered[1]][entered[0]] != self.solution[entered[1]][entered[0]]:
                    self.board[entered[1]][entered[0]] = 0
                self.entered_filled = []
        
            for sketched in self.sketch_filled:
                if self.board[sketched[1]][sketched[0]] != self.solution[sketched[1]][sketched[0]]:
                    self.board[sketched[1]][sketched[0]] = 0
                self.sketch_filled = []

            solve_board(self.board)


    def toggle_mode(self):
        if self.highlight_incorrect_mode:
            self.highlight_incorrect_mode = False
            self.incorrect_tracker = True
        else:
            self.highlight_incorrect_mode = True
            self.incorrect_tracker = False
        self.set_window_title()

    def set_window_title(self):
        if self.highlight_incorrect_mode:
            if self.difficulty == EASY:
                pygame.display.set_caption(WINDOW_TITLE + EASY_MODE_TITLE + HIGHLIGHT_ERROR_TITLE)
            elif self.difficulty == MEDIUM:
                pygame.display.set_caption(WINDOW_TITLE + MEDIUM_MODE_TITLE + HIGHLIGHT_ERROR_TITLE)
            elif self.difficulty == HARD:
                pygame.display.set_caption(WINDOW_TITLE + HARD_MODE_TITLE + HIGHLIGHT_ERROR_TITLE)
            elif self.difficulty == EVIL:
                pygame.display.set_caption(WINDOW_TITLE + EVIL_MODE_TITLE + HIGHLIGHT_ERROR_TITLE)
        else:
            if self.difficulty == EASY:
                pygame.display.set_caption(WINDOW_TITLE + EASY_MODE_TITLE + TRACK_ERROR_TITLE)
            elif self.difficulty == MEDIUM:
                pygame.display.set_caption(WINDOW_TITLE + MEDIUM_MODE_TITLE + TRACK_ERROR_TITLE)
            elif self.difficulty == HARD:
                pygame.display.set_caption(WINDOW_TITLE + HARD_MODE_TITLE + TRACK_ERROR_TITLE)
            elif self.difficulty == EVIL:
                pygame.display.set_caption(WINDOW_TITLE + EVIL_MODE_TITLE + TRACK_ERROR_TITLE)

    def format_time(self):
        seconds = self.play_time%60
        minutes = self.play_time//60
        hours = minutes//60

        def add_zero_in_front(time):
            if time < 10:
                return str(0) + str(time)
            else:
                return str(time)
        return str(hours) + ":" + add_zero_in_front(minutes) + ":" + add_zero_in_front(seconds)

    def draw_time(self, window):
        text = self.original_font.render("Time: " + self.format_time(), False, BLACK)
        window.blit(text, (WIDTH//2-85, 600))

    def draw_strikes(self, window):
        text = self.original_font.render("Strikes: " + ("X" * self.strikes), False, (255, 0, 0))
        window.blit(text, (20, 600))

    def reset_board(self):
        for entered in self.entered_filled:
            self.board[entered[1]][entered[0]] = 0
        
        for sketched in self.sketch_filled:
            self.board[sketched[1]][sketched[0]] = 0
            
        self.sketch_filled = []
        self.entered_filled = []
        self.strikes = 0
        self.solved = False
        self.solved_prompt = 0
        self.start_time = time.time()