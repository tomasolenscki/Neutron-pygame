from .constantes import RED, WHITE, SQUARE_SIZE, GREY, BLUE, GREEN, BORDA
import pygame

class Piece:
    PADDING = 20
    OUTLINE = 5

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + BORDA/2 + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + BORDA/2 + SQUARE_SIZE // 2
    
    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)