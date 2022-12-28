import numpy as np
# from math import log2
# from time import time

def enlarge(input):
    size = len(input)
    return np.hstack((np.zeros((size + 2, 1)), np.vstack((np.zeros((1, size)), input, np.zeros((1, size)))), np.zeros((size + 2, 1))))

def update(cells):
    cells = enlarge(cells)
    nxt = np.zeros(cells.shape)
    for r, c in np.ndindex(cells.shape):
        num_alive = np.sum(cells[r-1:r+2, c-1:c+2]) - cells[r, c]
        if (cells[r, c] and 2 <= num_alive <= 3) or (not cells[r, c] and num_alive == 3):
            nxt[r, c] = 1
    return nxt.astype(int)[1:-1, 1:-1]

def id(arr):
    return "".join(list(map(lambda x: str(int(x)), arr.flatten())))

def to_str(arr):
    up, down, left, right = 0, 0, 0, 0
    for i in arr:
        if i.any():
            break
        up += 1
    for i in arr[::-1]:
        if i.any():
            break
        down -= 1
    for i in arr.T:
        if i.any():
            break
        left += 1
    for i in arr.T[::-1]:
        if i.any():
            break
        right -= 1
    arr = arr[up:, left:] if down + right == 0 else\
          arr[up:, left:right] if down == 0 else\
          arr[up:down, left:] if right == 0 else\
          arr[up:down, left:right]
    return "".join(list(map(str, list(arr.flatten()))))

with open("output.txt", "w") as file:
    file.write("Algorithm test\nInput cell size = 6 * 6\n")
database = []
size = 6

# t0 = time()
for i in range(1, 2 ** (size ** 2)):
    # if 2 ** round(log2(i)) == i and i > 100000 and i != 0:
        # print(i, time()-t0)
    if i % (2 ** size) != 0:
        continue
    b = bin(i)[2:]
    sequence = "0" * ((size ** 2) - len(b)) + b
    arr = np.array(list(map(int, list(sequence)))).reshape((size, size))
    if arr.T[-1].any() or arr.T[0].any() or arr[-1].any() or arr[0].any():
        continue
    if to_str(arr) in database:
        continue
    with open("output.txt", "a") as file:
        t = 0
        data = id(arr)
        if len(data) <= 2:
            break
        while True:
            txt = id(arr)
            t += 1
            if len(txt) <= 2:
                break
            elif t > 1 and txt == data:
                if to_str(arr) not in database and to_str(arr.T) not in database\
                    and to_str(arr[:,::-1]) not in database and to_str(arr.T[:,::-1]) not in database:
                    file.write(str(arr)+"\n")
                    database.append(to_str(arr))
                break
            elif t > 20:
                break
            arr = update(arr)