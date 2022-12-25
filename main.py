import pygame
from constant import * #引入顏色、幀率
import init #初始化
import modify #修改
import update #包含更新跟畫上格子
from menu import MainMenu, Settings

def main(dimx, dimy, cellsize):
    pygame.init()
    display = pygame.Surface((dimx * cellsize, dimy * cellsize))
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("Game of Life")
    cells = init.init(dimx, dimy)
    clock = pygame.time.Clock()
    running = 1 #暫停狀態，預設1=運行
    status = "main" #status: main(menu), run, settings，預設為起始畫面
    current_menu = MainMenu(display, surface, dimx, dimy, cellsize, col_background)
    current_settings = Settings(display, surface, dimx, dimy, cellsize, col_background)

    while True:
        if status == "main":
            if current_menu.run_display and current_menu.run_code:
                current_menu.display_menu()
                pygame.display.update()
                # elif event.type == pygame.MOUSEBUTTONDOWN:
                #     mouse_pos = pygame.mouse.get_pos()
                #     if start_button.on(mouse_pos):
                #         print("Running the game...")
                #         status = "run"
                #         current_menu.run_display = False
                    # elif settings_button.on(mouse_pos):
            elif not current_menu.run_code:
                pygame.quit()
                return 0
            elif not current_menu.run_display:
                status = "run"
        elif status == "setting":
            #TODO
            pass
        elif status == "run":
            for event in pygame.event.get():
                # print(event.type)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0
                
                if event.type == 768:
                    # keys = pygame.key.get_pressed()
                    # if keys[pygame.K_SPACE]:
                    running = 0 if running else 1
                
                if event.type == pygame.MOUSEBUTTONDOWN: #點擊方格修改
                    mouse_pos = pygame.mouse.get_pos()
                    if modify.mouse_on_grid(mouse_pos, dimx, dimy, cellsize):
                        modify.modify(mouse_pos, cells, cellsize)
            clock.tick(FPS) #固定幀率
            surface.fill(col_grid)
            if running: 
                cells = update.update(surface, cells, dimx, dimy, cellsize, running) #如果沒有暫停的話就修改
            update.draw(surface, cells, dimx, dimy, cellsize)
            # pygame.draw.rect(surface, col_background, (1*cellsize, dimy * cellsize + 1*cellsize, 2*cellsize, 1.5*cellsize))
            pygame.display.update()

if __name__ == '__main__':
    main(96, 60, 10)