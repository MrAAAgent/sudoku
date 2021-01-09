import pygame
from constants import START_NEW_GAME_TITLE, START_NEW_GAME_MESSAGE

class Button:
    def __init__(self, position_x, position_y, width, height, text, confirmation_title=START_NEW_GAME_TITLE, confirmation_message=START_NEW_GAME_MESSAGE, colour=(73,73,73), hovered_colour=(189, 189, 189), function=None, params=None):
        self.image = pygame.Surface((width, height))
        self.position = (position_x,position_y)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position
        self.width = width
        self.height = height
        self.text = text
        self.confirmation_title = confirmation_title
        self.confirmation_message = confirmation_message
        self.colour = colour
        self.hovered_colour = hovered_colour
        self.function = function
        self.params = params
        self.hovered = False

    def update_button_state(self, mouse):
        if self.rect.collidepoint(mouse):
            self.hovered = True
        else:
            self.hovered = False

    def draw_button(self, window):
        self.image.fill(self.hovered_colour if self.hovered else self.colour)
        if self.text:
            self.draw_button_text(self.text)
        window.blit(self.image, self.position)


    def click(self):
        if self.params:
            self.function(self.params)
        else:
            self.function()
            

    def draw_button_text(self, text):
        font = pygame.font.SysFont("arial", 20, bold=1)
        text = font.render(text, False, (0,0,0))
        width, height = text.get_size()
        x = (self.width-width)//2
        y = (self.height-height)//2
        self.image.blit(text, (x, y))