import pygame

class Button:
    def __init__(self, position_x, position_y, width, height, text="", colour=(73,73,73), hovered_colour=(189, 189, 189), function=None, params=None):
        self.image = pygame.Surface((width, height))
        self.position = (position_x,position_y)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position
        self.text = text
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
        window.blit(self.image, self.position)