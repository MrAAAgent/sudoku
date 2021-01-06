import pygame
from solve import solve_board, valid_add
from constants import *
pygame.font.init()

#class Grid:
#def init(self):
#    self.rows = NUM_ROWS
#    self.columns = NUM_COLUMNS
#    self.width = WIDTH
#    self.height = HEIGHT
#    self.selected_square = None
#    self.getBoard()


def start_game():
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    board = Grid()
    typed = None
    running = True
    start_time = pygame.time.get_ticks()

    while running:
        play_time = round(pygame.time.get.ticks() - start_time)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # move to grid 
                elif event.key == pygame.K_RIGHT:
                    # move
                elif event.key == pygame.K_UP:
                    # move
                elif event.key == pygame.K_DOWN:
                    #move to grid
                
                if event.key == pygame.K_1:
                    typed = 1
                elif event.key == pygame.K_2:
                    typed = 2
                elif event.key == pygame.K_3:
                    typed = 3
                elif event.key == pygame.K_4:
                    typed = 4
                elif event.key == pygame.K_5:
                    typed = 5
                elif event.key == pygame.K_6:
                    typed = 6
                elif event.key == pygame.K_7:
                    typed = 7
                elif event.key == pygame.K_8:
                    typed = 8
                elif event.key == pygame.K_9:
                    typed = 9
                elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_RETURN:
                    typed = None
                    


                    



