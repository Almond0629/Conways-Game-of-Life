import pygame
from constant import *
import numpy as np
'''
這邊把更新跟畫格子拆開了，這樣比較好修改
'''
def update(surface, cells, dimx, dimy, cellsize, running): # cells: current status, cellsize: square size
    nxt = np.zeros((cells.shape[0], cells.shape[1]))
    if running:
        for r, c in np.ndindex(cells.shape):
            num_alive = np.sum(cells[r-1:r+2, c-1:c+2]) - cells[r, c] # 周圍還活著的
            if (cells[r, c] == 1 and min_num_alive <= num_alive <= max_num_alive) or (cells[r, c] == 0 and num_alive == num_repro):
                nxt[r, c] = 1
    return nxt

def draw(surface, nxt, dimx, dimy, cellsize):
    for r, c in np.ndindex(nxt.shape):
        num_alive = np.sum(nxt[r-1:r+2, c-1:c+2]) - nxt[r, c] # 周圍還活著的
        col = col_background
        if num_alive > 0:
            col = col_neighbor
        if (nxt[r, c] == 1 and 2 <= num_alive <= 3):
            col = col_alive
        elif nxt[r, c] == 1 and (num_alive < 2 or num_alive > 3):
            col = col_about_to_die
        # col = col if cells[r, c] == 1 or col == col_neighbor else col_background
        pygame.draw.rect(surface, col, (c*cellsize, r*cellsize, cellsize-1, cellsize-1)) #更新方格顏色