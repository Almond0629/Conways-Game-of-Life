import pygame
from constant import *

class Button:
    def __init__(self, x, y, content: str, fontsize):
        font = pygame.font.Font('8-BIT_WONDER.TTF', fontsize)
        self.text_surface = font.render(content, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect()
        self.w = self.text_surface.get_rect()[2]
        self.h = self.text_surface.get_rect()[3]
        self.x = x - self.w / 2
        self.y = y
        self.display = pygame.Surface((self.w, self.h))
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.display.fill(col_background)
        self.display.blit(self.text_surface, (self.rect.width/2 - self.text_rect.width/2, self.rect.height/2 - self.text_rect.height/2))

    
    def draw(self, surface):
        surface.blit(self.display, self.rect)
    
    def on(self, pos):
        return self.x <= pos[0] <= (self.x + self.w) and self.y <= pos[1] <= (self.y + self.h)