import pygame
import constant
from constant import col_background, col_grid #引入顏色、幀率
from init import init #初始化
import modify #修改
import update #包含更新跟畫上格子
from menu import MainMenu, Settings
from button import Button
from output import database

def main(dimx, dimy, cellsize):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('8-bit-universe.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    display = pygame.Surface((dimx * cellsize, dimy * cellsize))
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("Game of Life")
    cells = init(dimx, dimy)
    clock = pygame.time.Clock()
    running = True #暫停狀態，預設1=運行
    status = "main" #status: main(menu), run, settings，預設為起始畫面
    current_menu = MainMenu(display, surface, dimx, dimy, cellsize, col_background)
    
    title1 = Button(cellsize * (dimx - 13), cellsize * dimy / 2 - 270, 'Conway\'s', 40, col_grid)
    title2 = Button(cellsize * (dimx - 13), cellsize * dimy / 2 - 240, 'Game of Life', 40, col_grid)
    start_button = Button(cellsize * (dimx - 13), cellsize * dimy / 2 - 190, 'Start/Stop', 50, col_grid,large=True)
    edit_button = Button(cellsize * (dimx - 13), cellsize * dimy / 2 - 90, 'Editing mode', 35, col_grid)
    modify_down = Button(cellsize * (dimx - 13 - 8), cellsize * dimy / 2 - 50, '-', 70, col_grid,large=True)
    default_text = Button(cellsize * (dimx - 13), cellsize * dimy / 2 - 25, 'default', 30, col_grid)
    modify_up = Button(cellsize * (dimx - 13 + 8), cellsize * dimy / 2 - 50, '+', 70, col_grid,large=True)
    clear_button = Button(cellsize * (dimx - 13), cellsize * dimy / 2 + 20, 'Clear', 50, col_grid,large=True)
    reset_button = Button(cellsize * (dimx - 13), cellsize * dimy / 2 + 90, 'Reset', 50, col_grid,large=True)
    settings_button = Button(cellsize * (dimx - 13), cellsize * dimy / 2 + 160, 'Settings', 50, col_grid,large=True)
    menu_button = Button(cellsize * (dimx - 13), cellsize * dimy / 2 + 230, 'Menu', 50, col_grid,large=True)
    
    
    
    while True:
        if status == "main":
            if current_menu.run_display and current_menu.run_code:
                current_menu.display_menu()
                pygame.display.update()
            if not current_menu.run_code:
                pygame.quit()
                return 0
            if current_menu.goto_running:
                status = "run"
            if current_menu.goto_setting:
                status = "settings"
        elif status == "settings":
            current_settings = Settings(display, surface, dimx, dimy, cellsize, col_background)
            if current_settings.run_code and current_settings.run_display:
                current_settings.display_menu()
                pygame.display.update()
            if current_settings.goto_menu:
                status = "main"
                current_menu = MainMenu(display, surface, dimx, dimy, cellsize, col_background)
            if current_settings.goto_run:
                status = "run"
            if not current_settings.run_code:
                pygame.quit()
                return 0
        elif status == "run":
            for event in pygame.event.get():
                # print(event.type)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0
                
                if event.type == 768:
                    # keys = pygame.key.get_pressed()
                    # if keys[pygame.K_SPACE]:
                    running = False if running else True
                
                if event.type == pygame.MOUSEBUTTONDOWN: #點擊方格修改
                    mouse_pos = pygame.mouse.get_pos()
                    if modify.mouse_on_grid(mouse_pos, dimx, dimy, cellsize):
                        modify.modify(mouse_pos, cells, cellsize, dimx, dimy)
                    if start_button.on(mouse_pos):
                        running = False if running else True
                    # if edit_button.on(mouse_pos):
                    #     running = False
                    if modify_up.on(mouse_pos):
                        if constant.modify_number < len(database)-1:
                            constant.modify_number += 1
                        else:
                            constant.modify_number = -1
                    if modify_down.on(mouse_pos):
                        if constant.modify_number > -1:
                            constant.modify_number -= 1
                        else:
                            constant.modify_number = len(database)-1
                    if clear_button.on(mouse_pos):
                        cells.fill(0)
                    if reset_button.on(mouse_pos):
                        cells = init(dimx, dimy)
                    if settings_button.on(mouse_pos):
                        status = "settings"
                    if menu_button.on(mouse_pos):
                        status = "main"
                        current_menu = MainMenu(display, surface, dimx, dimy, cellsize, col_background)
            surface.fill(col_grid)
            # running_menu.display_menu()
            update.draw(surface, cells, dimx, dimy, cellsize)
            title1.draw(surface)
            title2.draw(surface)
            start_button.draw(surface)
            edit_button.draw(surface)
            modify_up.draw(surface)
            modify_down.draw(surface)
            clear_button.draw(surface)
            reset_button.draw(surface)
            settings_button.draw(surface)
            menu_button.draw(surface)
            if constant.modify_number < 0:
                default_text.draw(surface)
            else:
                modify.draw_example(surface, constant.modify_number, cellsize * (dimx - 13), cellsize * dimy / 2 -20, cellsize)
            if running: 
                cells = update.update(surface, cells, dimx, dimy, cellsize, running) #如果沒有暫停的話就修改
            # pygame.draw.rect(surface, col_background, (1*cellsize, dimy * cellsize + 1*cellsize, 2*cellsize, 1.5*cellsize))
            pygame.display.update()
            if constant.FPS > 0:
                clock.tick(constant.FPS) #固定幀率
            else:
                running = False

if __name__ == '__main__':
    main(96, 60, 10)