import pygame
import tkinter as tkinter
from tkinter import messagebox

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
        self.width = width
        self.height = height

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

    def click_new_game(self): 
        root = tkinter.Tk()
        root.withdraw() # hide the tkinter root window
        confirmation = tkinter.messagebox.askquestion('Start New Game','You will lose all progress on your current game. Start new game?')
        if confirmation == 'yes':
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

    def change_button_text(self):
        if self.text == "Solve":
            self.text == "New Game"
        else:
            self.text == "Solve"