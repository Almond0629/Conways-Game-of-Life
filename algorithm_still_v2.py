import numpy as np
from tqdm import tqdm
from textwrap import wrap
import pygame
from update import draw
from constant import col_grid

with open("still_output_5.txt", "w") as file:
    file.write("Still cells\nInput cell size = 6 * 6\n")
database = set()
progress = tqdm(total = 2 ** 36 - 1)
output = []
dimx, dimy, cellsize = 82, 50, 10 #顯示用
pygame.init() #顯示用
display = pygame.Surface((dimx * cellsize, dimy * cellsize)) #顯示用
surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize)) #顯示用
pygame.display.set_caption("Game of Life") #顯示用
display_arr = -np.ones((dimy, dimx)) #顯示用
count = 0 #顯示用

for i in range(1, 2 ** 36):
    progress.update(1)
    strcell = "0" * 6 + bin(i)[2:][::-1] + "0" * 6
    aug_strcell = "00".join(wrap(strcell, 6))
    l = len(aug_strcell)
    aug_nxt = "".join(["1" if (s := sum([int(aug_strcell[k]) for k in (j-9, j-8, j-7, j-1, j+1, j+7, j+8, j+9) if 0 <= k < l])) == 3 else "1" if s == 2 and int(aug_strcell[j]) else "0" for j in range(l)])
    nxt = "".join([i for n, i in enumerate(wrap(aug_nxt, 2)) if (n+1) % 4 != 0])
    if strcell == nxt and aug_nxt.count("1") == nxt.count("1"):
        nstrcell = strcell.strip("0")
        if nstrcell not in database:
            arr = np.array(list(nstrcell + "0" * (36 - len(nstrcell)))).reshape((6, 6))
            output.append(np.array(list(strcell + "0" * (36 - len(strcell)))).reshape((6, 6)))
            column, row = divmod(count, 6) #顯示用
            column %= 10 #顯示用
            display_arr[2+8*row:8+8*row, 2+8*column:8+8*column] = arr #顯示用
            surface.fill(col_grid) #顯示用
            draw(surface, display_arr, dimx, dimy, cellsize, True) #顯示用
            pygame.display.update() #顯示用
            count += 1 #顯示用
            for array in (arr, arr.T, arr[::-1], arr[::-1].T, arr.T[::-1], arr.T[::-1].T, arr[::-1].T[::-1], arr[::-1].T[::-1].T):
                database.add("".join(array.astype(str).flatten()).strip("0").rstrip("0"))
            # with open("still_output_5.txt", "a") as file:
            #     file.write("\n".join(i for i in wrap(strcell, 6) if i != "000000" and len(i) == 6) + "\n\n")
    for event in pygame.event.get(): #顯示用
        if event.type == pygame.QUIT: #顯示用
            pygame.quit() #顯示用

