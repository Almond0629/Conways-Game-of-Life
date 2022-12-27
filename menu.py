import pygame
import constant
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
        self.title_fontsize = 120
        self.fontsize = 70
        self.title1 = Button(self.x, self.y - 200, "Conway\'s", self.title_fontsize)
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
        self.x = self.w / 2
        self.y = self.h / 2
        self.fontsize = 60
        self.min_num_alive_setbutton = Button(self.x, self.y-150, f'Minimum limitaion to live: {constant.min_num_alive}', self.fontsize, align_left=True)
        self.max_num_alive_setbutton = Button(self.x, self.y-75, f'Maximum limitation to live: {constant.max_num_alive}', self.fontsize, align_left=True)
        self.num_repro_setbutton = Button(self.x, self.y, f'Reproduce condition: {constant.num_repro}', self.fontsize, align_left=True)
        self.framerate_setbutton = Button(self.x, self.y+75, f'frame per second: {constant.FPS}', self.fontsize, align_left=True)
        self.goto_menu_button = Button(self.x+200, self.y+200, 'Go to menu', self.fontsize)
        self.goto_run_button = Button(self.x-200, self.y+200, 'Start', self.fontsize)
        self.title = Button(self.x, self.y-250, 'Settings', self.fontsize+10)
        self.max_up = Button(self.x+350, self.y-75, '+', self.fontsize)
        self.max_down = Button(self.x+400, self.y-75, '-', self.fontsize)
        self.min_up = Button(self.x+350, self.y-150, '+', self.fontsize)
        self.min_down = Button(self.x+400, self.y-150, '-', self.fontsize)
        self.rep_up = Button(self.x+350, self.y, '+', self.fontsize)
        self.rep_down = Button(self.x+400, self.y, '-', self.fontsize)
        self.fps_up = Button(self.x+350, self.y+75, '+', self.fontsize)
        self.fps_down = Button(self.x+400, self.y+75, '-', self.fontsize)
    
    def display_menu(self): # displaying the menu
        self.run_display = True
        self.goto_menu = False
        self.goto_run = False
        self.run_code = True
        while self.run_display and self.run_code and not self.goto_menu and not self.goto_run:
            self.display.fill(self.color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_code = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.goto_menu_button.on(mouse_pos):
                        self.goto_menu = True
                    if self.goto_run_button.on(mouse_pos):
                        self.goto_run = True
                    if self.max_up.on(mouse_pos):
                        constant.max_num_alive += 1
                        self.max_num_alive_setbutton.update(f'Maximum limitation to live: {constant.max_num_alive}')
                    if self.max_down.on(mouse_pos) and constant.max_num_alive > 0:
                        constant.max_num_alive -= 1
                        self.max_num_alive_setbutton.update(f'Maximum limitation to live: {constant.max_num_alive}')
                    if self.min_up.on(mouse_pos):
                        constant.min_num_alive += 1
                        self.min_num_alive_setbutton.update(f'Minimum limitaion to live: {constant.min_num_alive}')
                    if self.min_down.on(mouse_pos):
                        constant.min_num_alive -= 1 and constant.min_num_alive > 0
                        self.min_num_alive_setbutton.update(f'Minimum limitaion to live: {constant.min_num_alive}')
                    if self.rep_up.on(mouse_pos):
                        constant.num_repro += 1
                        self.num_repro_setbutton.update(f'Reproduce condition: {constant.num_repro}')
                    if self.rep_down.on(mouse_pos) and constant.num_repro > 0:
                        constant.num_repro -= 1
                        self.num_repro_setbutton.update(f'Reproduce condition: {constant.num_repro}')
                    if self.fps_up.on(mouse_pos):
                        constant.FPS += 1
                        self.framerate_setbutton.update(f'frame per second: {constant.FPS}')
                    if self.fps_down.on(mouse_pos) and constant.FPS > 0:
                        constant.FPS -= 1
                        self.framerate_setbutton.update(f'frame per second: {constant.FPS}')
            buttons = [self.min_num_alive_setbutton, self.max_num_alive_setbutton, self.num_repro_setbutton, self.framerate_setbutton, self.goto_menu_button, self.goto_run_button, self.title, self.max_up, self.max_down, self.min_up, self.min_down, self.rep_up, self.rep_down, self.fps_up, self.fps_down]
            for button in buttons:
                button.draw(self.display)
            self.blit_screen()
    