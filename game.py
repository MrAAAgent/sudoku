import pygame, sys
from button import *
from solve import valid_add
from puzzle import *
from constants import *
pygame.font.init()

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Sudoku")
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = False
        self.board = []
        self.solution = []
        self.difficulty = None
        self.original_filled = []
        self.sketch_filled = []
        self.entered_filled = []
        self.solved = False
        self.selected_square = None
        self.mouse_position = None
        self.font = pygame.font.SysFont("comicsans", 40)
        self.play_time = True
        self.new_game_buttons = []
        self.toggle_buttons = []
        self.end_buttons = []
        self.highlight_incorrect_mode = True
        self.incorrect_tracker = False
        self.incorrect_submissions = 0
        self.set_board(EASY)
        
    def start_game(self):                
        self.startup()
        #self.start_time = pygame.time.get_ticks()
        self.running = True
        while self.running:
            if self.play_time:
                self.handle_events()
                self.update_state()
                self.draw()  
                #self.play_time = round(pygame.time.get.ticks() - start_time)
        pygame.quit()
        sys.quit()      

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.selected_square = self.board_position()
                if not self.selected_square or self.selected_square in self.original_filled:
                    self.selected_square = None
                
                for button in self.new_game_buttons:
                    if button.hovered:
                        button.click_new_game()

            if event.type == pygame.KEYDOWN and self.selected_square != None:
                try:
                    int(event.unicode)
                    if int(event.unicode) > 0:
                        self.board[self.selected_square[1]][self.selected_square[0]] = int(event.unicode)
                        self.sketch_filled.append(self.selected_square)
                except:
                    if event.key == pygame.K_BACKSPACE:
                        self.board[self.selected_square[1]][self.selected_square[0]] = 0
                        if self.selected_square in self.sketch_filled:
                            self.sketch_filled.remove(self.selected_square)
                        elif self.selected_square in self.entered_filled:
                            self.entered_filled.remove(self.selected_square)
                    elif event.key == pygame.K_RETURN:
                        for sketch in self.sketch_filled:
                            if self.selected_square == sketch:
                                self.sketch_filled.remove(sketch)
                                self.entered_filled.append(sketch)
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
        for button in self.new_game_buttons:
            button.update_button_state(self.mouse_position)

        if self.highlight_incorrect_mode:
            self.incorrect_submissions = []
            self.check_for_incorrect()

    def check_for_incorrect(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLUMNS):
                if self.board[r][c] != 0 and self.board[r][c] != self.solution[r][c]:
                    self.incorrect_submissions.append((c, r))

    def draw(self):
        self.window.fill(WHITE)

        for button in self.new_game_buttons:
            button.draw_button(self.window)

        if self.selected_square:
            self.draw_selected(self.window, self.selected_square)
        
        self.draw_incorrect(self.window)

        self.draw_board(self.window)
        self.draw_board_numbers(self.window)
        pygame.display.update()


    def draw_board(self, window):
        pygame.draw.rect(window, BLACK, (BOARD_POSITION[0], BOARD_POSITION[1], WIDTH-150, HEIGHT-150), 2)
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
                    self.draw_number(window, str(self.board[r][c]), position)

    def draw_selected(self, window, position):
        pygame.draw.rect(window, LIGHT_BLUE, (position[0]*CELL_SIZE+BOARD_POSITION[0], position[1]*CELL_SIZE+BOARD_POSITION[1], CELL_SIZE, CELL_SIZE))

    
    def draw_incorrect(self, window):
        for position in self.incorrect_submissions:
            pygame.draw.rect(window, INCORRECT_RED, (position[0]*CELL_SIZE+BOARD_POSITION[0], position[1]*CELL_SIZE+BOARD_POSITION[1], CELL_SIZE, CELL_SIZE))
    

    def load_buttons(self):
        self.new_game_buttons.append(Button(20, 40, WIDTH//7, 40,
                                            function=self.solve,  
                                            colour=(27,142,207),
                                            text="Check"))
        self.new_game_buttons.append(Button(140, 40, WIDTH//7, 40,
                                            colour=(117,172,112),
                                            function=self.set_board,
                                            params=EASY,
                                            text="Easy"))
        self.new_game_buttons.append(Button(WIDTH//2-(WIDTH//7)//2, 40, WIDTH//7, 40,
                                            colour=(204,197,110),
                                            function=self.set_board,
                                            params=MEDIUM,
                                            text="Medium"))
        self.new_game_buttons.append(Button(380, 40, WIDTH//7, 40,
                                            colour=(199,129,48),
                                            function=self.set_board,
                                            params=HARD,
                                            text="Hard"))
        self.new_game_buttons.append(Button(500, 40, WIDTH//7, 40,
                                            colour=(207,68,68),
                                            function=self.set_board,
                                            params=EVIL,
                                            text="Evil"))



    def draw_number(self, window, number, position):
        printed_number = self.font.render(number, False, BLACK)
        adjusted_position = (position[0] + (CELL_SIZE - printed_number.get_width())//2, position[1] + (CELL_SIZE - printed_number.get_height())//2)
        window.blit(printed_number, adjusted_position)


    def startup(self):
        self.load_buttons()


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


    def solve(self):
        pass
