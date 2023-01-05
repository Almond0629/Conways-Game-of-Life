import pygame 
import numpy as np
import constant
from output import database
from button import Button

def mouse_on_grid(mouse_pos, dimx, dimy, cellsize):
    return  (dimx - 27) * cellsize > mouse_pos[0] > 0 and dimy * cellsize > mouse_pos[1] > 0
    
def modify(mouse_pos, cells, cellsize, dimx, dimy):
    cell_pos = (mouse_pos[1] // cellsize, mouse_pos[0] // cellsize)
    if constant.modify_number < 0:
        cells[cell_pos[0], cell_pos[1]] = 0 if cells[cell_pos[0], cell_pos[1]]==1 else 1
    else:
        size = database[0].shape[0]
        if (dimx - 26 - size) > cell_pos[1] and (dimy - size) > cell_pos[0]:
            # cells = cells.astype(int)
            cells[cell_pos[0]:cell_pos[0]+size, cell_pos[1]:cell_pos[1]+size] |= database[constant.modify_number]
            print(cells[cell_pos[0]:cell_pos[0]+size, cell_pos[1]:cell_pos[1]+size])

def draw_example(surface, index, cx, cy, cellsize):
    arr = database[index]
    size = arr.shape[0]
    ori_x = cx - (cellsize*size)/2
    ori_y = cy - (cellsize*size)/2
    for r in range(size):
        for c in range(size):
            if arr[r, c] == 1:
                pygame.draw.rect(surface, constant.col_alive, (ori_x+c*cellsize, ori_y+r*cellsize, cellsize-1, cellsize-1))
            else:
                pygame.draw.rect(surface, constant.col_background, (ori_x+c*cellsize, ori_y+r*cellsize, cellsize-1, cellsize-1))
    
        