import pygame
from constant import *

class Button:
    def __init__(self, x, y, content: str, fontsize, color=col_background, align_left=False, large=False):
        font = pygame.font.Font(fonttype, fontsize)
        self.fontsize = fontsize
        self.text_surface = font.render(content, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect()
        self.w = self.text_surface.get_rect()[2]
        self.h = self.text_surface.get_rect()[3]
        if large:
            self.w += 30
            self.h += 30
        self.x = x - self.w / 2
        self.y = y
        self.align_left = align_left
        self.display = pygame.Surface((self.w, self.h))
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        if align_left:
            self.rect.left = 50
        self.display.fill(color)
        self.display.blit(self.text_surface, (self.rect.width/2 - self.text_rect.width/2, self.rect.height/2 - self.text_rect.height/2))

    
    def draw(self, surface):
        surface.blit(self.display, self.rect)
    
    def on(self, pos):
        return self.x <= pos[0] <= (self.x + self.w) and self.y <= pos[1] <= (self.y + self.h)
    
    def update(self, content):
        self = self.__init__(self.x, self.y, content, self.fontsize, align_left=self.align_left, large=True)