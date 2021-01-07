import pygame, sys
from button import *
from solve import solve_board, valid_add
from constants import *
pygame.font.init()

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Sudoku")
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.board = TEST_BOARD
        self.selected_square = None
        self.mouse_position = None
        self.font = pygame.font.SysFont("arial", CELL_SIZE//2)
        self.play_time = True
        self.play_buttons = []
        self.menu_buttons = []
        self.end_buttons = []
        self.load_buttons()
        
    def start_game(self):
        #self.start_time = pygame.time.get_ticks()

        while self.running:
            if self.play_time:
                self.handle_events()
                self.update_state()
                self.draw()  
                #self.play_time = round(pygame.time.get.ticks() - start_time)
        pygame.quit()
        #sys.quit()      

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.selected_square = self.board_position()
                if not self.selected_square:
                    self.selected_square = None

            #if event.type == pygame.KEYDOWN:
            #    if event.key == pygame.K_LEFT:
                    # move to grid 
            #    elif event.key == pygame.K_RIGHT:
                    # move
            #    elif event.key == pygame.K_UP:
                    # move
            #    elif event.key == pygame.K_DOWN:
                    #move to grid
                
            #    if event.key == pygame.K_1:
            #        typed = 1
            #    elif event.key == pygame.K_2:
            #        typed = 2
            #    elif event.key == pygame.K_3:
            #        typed = 3
            #    elif event.key == pygame.K_4:
            #        typed = 4
            #    elif event.key == pygame.K_5:
            #        typed = 5
            #    elif event.key == pygame.K_6:
            #        typed = 6
            #    elif event.key == pygame.K_7:
            #        typed = 7
            #    elif event.key == pygame.K_8:
            #        typed = 8
            #    elif event.key == pygame.K_9:
            #        typed = 9
            #    elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_RETURN:
            #        typed = None 

    def board_position(self):
        if self.mouse_position[0] < BOARD_POSITION[0] or self.mouse_position[0] > BOARD_POSITION[0]+BOARD_SIZE:
            return False
        elif self.mouse_position[1] < BOARD_POSITION[1] or self.mouse_position[1] > BOARD_POSITION[1]+BOARD_SIZE:
            return False
        return ((self.mouse_position[0]-BOARD_POSITION[0])//CELL_SIZE, (self.mouse_position[1]-BOARD_POSITION[1])//CELL_SIZE)

    def update_state(self):
        self.mouse_position = pygame.mouse.get_pos()
        for button in self.play_buttons:
            button.update_button_state(self.mouse_position)

    def draw(self):
        self.window.fill(WHITE)

        for button in self.play_buttons:
            button.draw_button(self.window)

        if self.selected_square:
            self.draw_selected(self.window, self.selected_square)

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
        pass

    def draw_selected(self, window, position):
        pygame.draw.rect(window, LIGHT_BLUE, (position[0]*CELL_SIZE+BOARD_POSITION[0], position[1]*CELL_SIZE+BOARD_POSITION[1], CELL_SIZE, CELL_SIZE))

    def load_buttons(self):
        self.play_buttons.append(Button(20,40,100,40))

    def draw_text(self, window, text, position):
        font = self.font.render(text, False, BLACK)
        window.blit(font, position)