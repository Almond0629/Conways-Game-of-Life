import numpy as np
from tqdm import tqdm

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

with open("still_output.txt", "w") as file:
    file.write("Algorithm test\nInput cell size = 6 * 6\n")
database = []
size = 6
progress = tqdm(total=2**(size**2)-1)

for i in range(1, 2 ** (size ** 2)):
    progress.update(1)
    if i % (2 ** size) != 0:
        continue
    b = bin(i)[2:]
    sequence = "0" * ((size ** 2) - len(b)) + b
    arr = np.array(list(map(int, list(sequence)))).reshape((size, size)).astype(int)
    if arr.T[-1].any() or arr.T[0].any() or arr[-1].any() or arr[0].any():
        continue
    if np.array_equal(arr, update(arr)) and to_str(arr) not in database:
        database += [to_str(arr), to_str(arr[:,::-1]), to_str(arr.T), to_str(arr[:,::-1].T)]
        with open("still_output.txt", "a") as file:
            file.write(np.array2string(arr) + "\n")

# result (i <= 1E8):
"""
Algorithm test
Input cell size = 6 * 6
[[0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 1 1 0]
 [0 0 0 1 1 0]
 [0 0 0 0 0 0]]
[[0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 1 0 1 1 0]
 [0 1 1 0 1 0]
 [0 0 0 0 0 0]]
[[0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 1 0 0]
 [0 0 1 0 1 0]
 [0 0 0 1 0 0]
 [0 0 0 0 0 0]]
[[0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 1 0 0]
 [0 0 1 0 1 0]
 [0 0 0 1 1 0]
 [0 0 0 0 0 0]]
[[0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 1 1 0]
 [0 0 1 0 1 0]
 [0 0 1 1 0 0]
 [0 0 0 0 0 0]]
[[0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 1 1 0]
 [0 1 0 0 1 0]
 [0 1 1 0 0 0]
 [0 0 0 0 0 0]]
[[0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 1 1 0 0]
 [0 0 1 0 1 0]
 [0 0 0 1 0 0]
 [0 0 0 0 0 0]]     # duplicate
[[0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 1 1 0 0]
 [0 1 0 0 1 0]
 [0 0 1 1 0 0]
 [0 0 0 0 0 0]]
[[0 0 0 0 0 0]
 [0 0 0 0 1 0]
 [0 0 1 1 1 0]
 [0 1 0 0 0 0]
 [0 1 1 0 0 0]
 [0 0 0 0 0 0]]
[[0 0 0 0 0 0]
 [0 0 0 1 0 0]
 [0 0 1 0 1 0]
 [0 1 0 0 1 0]
 [0 0 1 1 0 0]
 [0 0 0 0 0 0]]
[[0 0 0 0 0 0]
 [0 0 0 1 0 0]
 [0 0 1 0 1 0]
 [0 1 0 1 0 0]
 [0 0 1 0 0 0]
 [0 0 0 0 0 0]]
[[0 0 0 0 0 0]
 [0 0 0 1 0 0]
 [0 0 1 0 1 0]
 [0 1 0 1 0 0]
 [0 1 1 0 0 0]
 [0 0 0 0 0 0]]
"""