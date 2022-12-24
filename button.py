import pygame
from constant import *

class button:
    def __init__(self, x, y, wx, wy, col, text: str, fontsize):
        self.x = x
        self.y = y
        self.wx = wx
        self.wy = wy
        self.col = col
        self.text = text
        self.font = pygame.font.SysFont(fonttype, fontsize)
        self.surface = pygame.Surface((self.wx, self.wy))
        self.rect = pygame.Rect(self.x, self.y, self.wx, self.wy)
        self.surf = self.font.render(self.text, True, (20, 20, 20))
        self.surface.fill(col)
        self.surface.blit(self.surf, [
            self.rect.width/2 - self.surf.get_rect().width/2,
            self.rect.height/2 - self.surf.get_rect().height/2
        ])
    
    def draw(self, surface):
        surface.blit(self.surface, self.rect)
    
    def on(self, pos):
        return self.x <= pos[0] <= (self.x + self.wx) and self.y <= pos[1] <= (self.y + self.wy)