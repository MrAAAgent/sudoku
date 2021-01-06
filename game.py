import pygame, sys
from solve import solve_board, valid_add
from constants import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Sudoku")
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.board = TEST_BOARD
        #self.selected_square = None
        self.running = True
        #self.start_time = None
        
    def start_game(self):
        #self.start_time = pygame.time.get_ticks()

        while self.running:
           # self.play_time = round(pygame.time.get.ticks() - start_time)
            self.handle_events()
            self.update_state()
            self.draw()  

        #pygame.quit()
        #sys.quit()      

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
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

    def update_state(self):
        pass

    def draw(self):
        self.window.fill(WHITE)
        self.draw_board(self.window)
        pygame.display.update()

    def draw_board(self, window):
        pygame.draw.rect(window, BLACK, (BOARD_POSITION[0], BOARD_POSITION[1], WIDTH-120, HEIGHT-120), 2)


