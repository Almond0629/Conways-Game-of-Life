"""
Current progress:
- mouse input:
  - BUTTONDOWN, BUTTONUP: hold between
  - visible True/False
- keyboard input:
  - SPACE: start(continue)/pause
  - BACKSPACE: clear
Target:
- mouse input:
  - scroll
  - change appearance
  - 
- keyboard input:
  - 
"""

import pygame
import numpy as np
from pygame.locals import MOUSEBUTTONDOWN, MOUSEBUTTONUP

col_about_to_die = (200, 200, 225)
col_alive = (255, 255, 215)
col_background = (10, 10, 40)
col_grid = (30, 30, 60)

def update(surface, cur, sz):
    nxt = np.zeros((cur.shape[0], cur.shape[1]))

    for r, c in np.ndindex(cur.shape):
        num_alive = np.sum(cur[r-1:r+2, c-1:c+2]) - cur[r, c]

        if cur[r, c] == 1 and num_alive < 2 or num_alive > 3:
            col = col_about_to_die
        elif (cur[r, c] == 1 and 2 <= num_alive <= 3) or (cur[r, c] == 0 and num_alive == 3):
            nxt[r, c] = 1
            col = col_alive

        col = col if cur[r, c] == 1 else col_background
        pygame.draw.rect(surface, col, (c*sz, r*sz, sz-1, sz-1))

    return nxt

def surface_restart(surface, cells, cellsize):
    surface.fill(col_grid)
    for r, c in np.ndindex(cells.shape):
        pygame.draw.rect(surface, col_background, (c*cellsize, r*cellsize, cellsize-1, cellsize-1))


def init(dimx, dimy):
    cells = np.zeros((dimy, dimx))
    # pattern = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    #                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    #                     [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
    #                     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
    #                     [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    #                     [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    #                     [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    #                     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    #                     [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]);
    # pos = (3,3)
    # cells[pos[0]:pos[0]+pattern.shape[0], pos[1]:pos[1]+pattern.shape[1]] = pattern
    return cells

def main(dimx, dimy, cellsize):
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("John Conway's Game of Life")
    pygame.mouse.set_visible(True)

    cells = init(dimx, dimy)
    mouse_drag = False
    do_update = False

    surface_restart(surface, cells, cellsize)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == MOUSEBUTTONDOWN:
                mouse_drag = True
            elif event.type == MOUSEBUTTONUP:
                mouse_drag = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mouse.set_visible(not pygame.mouse.get_visible())
                    do_update = not do_update
                if event.key == pygame.K_BACKSPACE:
                    pygame.mouse.set_visible(True)
                    cells = np.zeros((dimy, dimx))
                    mouse_drag = False
                    do_update = False
                    surface_restart(surface, cells, cellsize)
                # if event.key == pygame.K_?:

        if mouse_drag:
            j = pygame.mouse.get_pos()[1] // cellsize
            i = pygame.mouse.get_pos()[0] // cellsize
            cells[j][i] = 1
            pygame.draw.rect(surface, col_alive, (i*cellsize, j*cellsize, cellsize-1, cellsize-1))
        
        pygame.display.update()

        if do_update:
            cells = update(surface, cells, cellsize)

if __name__ == "__main__":
    main(120, 90, 8)