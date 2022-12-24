import pygame
from constant import * #引入顏色、幀率
import init #初始化
import modify #修改
import update #包含更新跟畫上格子
from button import button

def main(dimx, dimy, cellsize):
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("Game of Life")
    cells = init.init(dimx, dimy)
    clock = pygame.time.Clock()
    running = 1 #暫停狀態，預設1=運行
    status = "main" #status: main(menu), run, settings，預設為起始畫面
    start_button = button(0, 0, 400, 200, '#00FF00', 'start', 100) #測試用起始按鈕
    quit_button = button(0, 200, 400, 200, '#FF0000', 'quit', 20) #測試用結束按鈕
    
    while True:
        if status == "main":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if start_button.on(mouse_pos):
                        print("run")
                        status = "run"
                    elif quit_button.on(mouse_pos):
                        pygame.quit()
                        return 0
            surface.fill(col_background)
            start_button.draw(surface)
            quit_button.draw(surface)
            pygame.display.update()
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