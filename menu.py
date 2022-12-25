import pygame
from constant import *
from button import Button

class Menu: # class for all menus
    def __init__(self, display, surface, dimx, dimy, cellsize, color):
        self.w = dimx * cellsize # width of the display window
        self.h = dimy * cellsize
        self.display = display #same displays as the main code
        self.surface = surface
        self.run_code = True # variable for deciding if the code should keep running
        self.run_display = True # variable for deciding if the code should keep displaying this menu
        self.color = color

    def blit_screen(self):
        self.surface.blit(self.display, (0,0))
        pygame.display.update()


class MainMenu(Menu): # class for the main menu
    def __init__(self, display, surface, dimx, dimy, cellsize, color):
        Menu.__init__(self, display, surface, dimx, dimy, cellsize, color)
        self.x = self.w / 2
        self.y = self.h / 2
        self.title_fontsize = 60
        self.fontsize = 30
        self.title1 = Button(self.x, self.y - 200, "Conway's", self.title_fontsize)
        self.title2 = Button(self.x, self.y - 100, "Game of Life", self.title_fontsize)
        self.start_button = Button(self.x, self.y + 50, 'Start', self.fontsize)
        self.settings_button = Button(self.x, self.y + 130, 'Settings', self.fontsize)

    def display_menu(self): # displaying the menu
        self.run_display = True
        self.run_code = True
        while self.run_display and self.run_code:
            self.display.fill(self.color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_code = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.start_button.on(mouse_pos):
                        print("Running the game...")
                        self.run_display = False
            self.title1.draw(self.display)
            self.title2.draw(self.display)
            self.start_button.draw(self.display)
            self.settings_button.draw(self.display)
            self.blit_screen()

