import numpy as np

size = 8
cells = np.zeros((size, size))
cells = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],])

temp = cells
r, c = cells.shape
bigcells = np.zeros((r+2, c+2))
bigcells.T[1:-1].T[1:-1] = temp
flatcells = bigcells.flatten()
c += 2

def split(cells):
    group = []
    global result
    for i in range(len(cells)):
        if cells[i] == 1:
            group.append([])
            group[-1].append(func(i))
    newgroup = []
    for j in group:
        newgroup += [flat(j)]
        result = []
    return [[j for j in i if type(j) != list] for i in newgroup]

def func(i):
    flatcells[i] = 0
    return [divmod(i, c)[::-1]] + [func(j) for j in (i-c-1, i-c, i-c+1, i-1, i+1, i+c-1, i+c, i+c+1) if flatcells[j] == 1]

result = []
def flat(list_):
    global result
    for i in list_:
        result += [flat(i)] if type(i) == list else [i]
    return result

def create_block(list_):
    blocks = []
    for i in list_:
        xmin, xmax, ymin, ymax = i[0][0], i[0][0], i[0][1], i[0][1]
        for j in i:
            xmin, xmax, ymin, ymax = min(xmin, j[0]), max(xmax, j[0]), min(ymin, j[1]), max(ymax, j[1])
        xmin, xmax, ymin, ymax = max(xmin-1, 0), min(xmax+2, c+2), max(ymin-1, 0), min(ymax+2, r+2)
        newcells = np.zeros((r+2, c))
        newcells.T[1:-1].T[1:-1] = cells
        block = np.zeros((size+2, size+2))
        block.T[:xmax-xmin].T[:ymax-ymin] = newcells.T[xmin:xmax].T[ymin:ymax]
        block = block.T[1:-1].T[1:-1]
        blocks.append((xmin, ymin, block))
    return blocks

def record(blocks):
    database = []
    for block in blocks:
        b = block[2]
        database.append((block[0], block[1], "".join(list(map(lambda x: str(int(x)), b.flatten())))))
    return database

print(record(create_block(split(flatcells))))