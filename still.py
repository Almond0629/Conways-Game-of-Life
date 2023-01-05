import numpy as np
from tqdm import tqdm
from textwrap import wrap
import pygame
from update import draw
import constant
from constant import col_grid

constant.max_num_alive = 3
constant.min_num_alive = 2
constant.num_repro = 3
database = set()
size = 4
maximum = 2 ** 18 #設定最多跑的格子數上限
progress = tqdm(total = min(maximum, 2**(size**2)-1))
output = []
dimx, dimy, cellsize = (size+2)*10+2, (size+2)*6+2, 80/(size+2) #顯示用
pygame.init() #顯示用
display = pygame.Surface((dimx * cellsize, dimy * cellsize)) #顯示用
surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize)) #顯示用
pygame.display.set_caption("Game of Life") #顯示用
display_arr = -np.ones((dimy, dimx)) #顯示用
count = 0 #顯示用

with open("output.py", "w") as file:
    file.write("import numpy as np\nsize = {}\ndatabase = [".format(size))
for i in range(1, min(maximum, 2 ** (size ** 2))):
    progress.update(1)
    strcell = "0" * size + bin(i)[2:][::-1] + "0" * size
    aug_strcell = "00".join(wrap(strcell, size))
    l = len(aug_strcell)
    aug_nxt = "".join(["1" if (s := sum([int(aug_strcell[k]) for k in (j-(size+3), j-(size+2), j-(size+1), j-1, j+1, j+(size+1), j+(size+2), j+(size+3)) if 0 <= k < l])) == constant.num_repro and not int(aug_strcell[j]) else "1" if constant.min_num_alive <= s <= constant.max_num_alive and int(aug_strcell[j]) else "0" for j in range(l)])
    nxt = "".join([i for n, i in enumerate(wrap(aug_nxt, 2)) if (n+1) % (size//2+1) != 0])
    if strcell == nxt and aug_nxt.count("1") == nxt.count("1"):
        nstrcell = strcell.strip("0")
        if nstrcell not in database:
            arr = np.array(list(nstrcell + "0" * ((size ** 2) - len(nstrcell)))).reshape((size, size))
            oarr = np.array(list(strcell[size:] + "0" * (size ** 2)))[:size**2].reshape((size, size))
            column, row = divmod(count, 6) #顯示用
            column %= 10 #顯示用
            display_arr[2+(size+2)*row:(size+2)+(size+2)*row, 2+(size+2)*column:(size+2)+(size+2)*column] = oarr#np.vstack((oarr[1:], np.array([0] * size).reshape((1, size)))) #顯示用
            surface.fill(col_grid) #顯示用
            draw(surface, display_arr, dimx, dimy, cellsize, True) #顯示用
            pygame.display.update() #顯示用
            count += 1 #顯示用
            for array in (arr, arr.T, arr[::-1], arr[::-1].T, arr.T[::-1], arr.T[::-1].T, arr[::-1].T[::-1], arr[::-1].T[::-1].T):
                database.add("".join(array.astype(str).flatten()).strip("0").rstrip("0"))
            with open("output.py", "a") as file:
                file.write("np.array(list('" + (x := "".join(i for i in wrap(strcell, size) if i != "0" * size and len(i) == size)) + "".join(["0" * size * (size - len(x) // size)]) + "')).astype(int).reshape((size, size)),")
    for event in pygame.event.get(): #顯示用
        if event.type == pygame.QUIT: #顯示用
            pygame.quit() #顯示用
with open("output.py", "a") as file:
    file.write("]\n#for i in database:\n#   print(i)")
while True:
    for event in pygame.event.get(): #顯示用
        if event.type == pygame.QUIT: #顯示用
            pygame.quit() #顯示用
    
    draw(surface, display_arr, dimx, dimy, cellsize, True) #顯示用
    pygame.display.update() #顯示用
