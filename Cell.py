import pygame
class Cell:
    def __init__(self, row, col, x, y, r):
        self.rect = pygame.Rect(x, y, r, r)
        self.row = row
        self.col = col
    
    def get_row_col(self):
        return (self.row, self.col)