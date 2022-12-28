# import pygame 
# import numpy as np
from constant import *

def mouse_on_grid(mouse_pos, dimx, dimy, cellsize):
    return  (dimx - 27) * cellsize > mouse_pos[0] > 0 and dimy * cellsize > mouse_pos[1] > 0
    
def modify(mouse_pos, cells, cellsize):
    cell_pos = (mouse_pos[1] // cellsize, mouse_pos[0] // cellsize)
    cells[cell_pos[0], cell_pos[1]] = 0 if cells[cell_pos[0], cell_pos[1]]==1 else 1