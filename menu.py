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
        self.title1 = Button(self.x, self.y - 200, "Conway s", self.title_fontsize)
        self.title2 = Button(self.x, self.y - 100, "Game of Life", self.title_fontsize)
        self.start_button = Button(self.x, self.y + 50, 'Start', self.fontsize)
        self.settings_button = Button(self.x, self.y + 130, 'Settings', self.fontsize)
        self.quit_button = Button(self.x, self.y + 210, 'Quit', self.fontsize)

    def display_menu(self): # displaying the menu
        self.run_display = True
        self.run_code = True
        self.goto_setting = False
        self.goto_running = False
        while self.run_display and self.run_code:
            self.display.fill(self.color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_code = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.start_button.on(mouse_pos):
                        print("Running the game...")
                        self.goto_running = True
                        self.run_display = False
                    elif self.quit_button.on(mouse_pos):
                        print("Quitting the game")
                        self.run_code = False
                    elif self.settings_button.on(mouse_pos):
                        print('Go to the game settings')
                        self.goto_setting = True
                        self.run_display = False
            self.title1.draw(self.display)
            self.title2.draw(self.display)
            self.start_button.draw(self.display)
            self.settings_button.draw(self.display)
            self.quit_button.draw(self.display)
            self.blit_screen()
class Settings(Menu):
    def __init__(self, display, surface, dimx, dimy, cellsize, color):
        Menu.__init__(self, display, surface, dimx, dimy, cellsize, color)
        self.x = self.w/2
        self.y = self.h/2
        self.fontsize = 30
        self.max_num_alive_setbutton = Button(self.x, self.y-200, 'Maximum limitaion to live', self.fontsize)
        self.max_num_alive_setbutton = Button(self.x, self.y-100, 'Minimum limotation to live', self.fontsize)
        self.num_repro_setbutton = Button(self.x, self.y, 'Reproduce condition', self.fontsize)
        self.goto_menu_button = Button(self.x+200, self.y+200, 'Goto menu', self.fontsize)
    
    def display_menu(self): # displaying the menu
        self.run_display = True
        self.goto_menu = False
        self.run_code = True
        while self.run_display and self.run_code and not self.goto_menu:
            self.display.fill(self.color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_code = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.goto_menu_button.on(mouse_pos):
                        self.goto_menu = True
            self.max_num_alive_setbutton.draw(self.display)
            self.max_num_alive_setbutton.draw(self.display)
            self.num_repro_setbutton.draw(self.display)
            self.goto_menu_button.draw(self.display)
            self.blit_screen()
    