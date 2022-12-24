# import pygame 
# import numpy as np
from constant import *

def mouse_on_grid(mouse_pos, dimx, dimy, cellsize):
    return mouse_pos[0] > 0 and mouse_pos[0] < dimx * cellsize and mouse_pos[1] > 0 and mouse_pos[1] < dimy * cellsize
    
def modify(mouse_pos, cells, cellsize):
    cell_pos = (mouse_pos[1] // cellsize, mouse_pos[0] // cellsize)
    cells[cell_pos[0], cell_pos[1]] = 0 if cells[cell_pos[0], cell_pos[1]]==1 else 1