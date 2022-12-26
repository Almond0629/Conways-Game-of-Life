import numpy as np
from copy import deepcopy
# 初始化大小(非必要)
size = 10
inputcells = np.zeros((size, size))
# 自訂輸入，
# 這個地方之後會套用000...000, 000...001, 000...010等的序列下去跑
inputcells = np.array([ [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ])
# 原本的cells上下左右各增加一排0
bigcells = np.hstack((np.zeros((12, 1)), np.vstack((np.zeros((1, 10)), inputcells, np.zeros((1, 10)))), np.zeros((12, 1))))
bigcellscopy = deepcopy(bigcells)

# 將inputcells轉成一個list，其中每一項是一個set，裝有一群連接在一起的點
# 連接的定義：在九宮格內
def split(cells):
    # 紀錄cells長寬
    r, c = cells.shape
    # 將1變成該點座標
    temp = np.arange(r * c).reshape((r, c))
    cells *= temp
    # 扁平化
    cells = cells.flatten()
    # 輸出序列
    group = []

    def func(i):
        # 括弧內為該點(i)附近九宮格(不含自己)
        for j in (i-c-1, i-c, i-c+1, i-1, i+1, i+c-1, i+c, i+c+1):
            # 檢測非0的格子(j)
            if cells[int(j)] != 0:
                # 計算座標，加入至group
                d = divmod(cells[int(j)], c)
                group[-1].add((int(d[1]), int(d[0])))
                # 該點(j)設為0(避免重複計算或無窮迴圈)
                cells[int(j)] = 0
                # 對j套用func，即執行該點(j)附近的九宮格
                func(j)
    
    # 將cells跑過一輪，因為同個group的點會一次跑完，然後全部變成0，所以不會跑重複的
    for i in cells:
        # 這邊跟func差不多
        if i != 0:
            d = divmod(cells[int(i)], c)
            group.append(set())
            group[-1].add((int(d[1]), int(d[0])))
            func(i)
    return group

# 將split傳出的list轉換成另一個list
def create_block(list_):
    # 輸出序列
    blocks = []
    # 將array扁平化後轉成str(丟至database)
    def id(arr):
        return "".join(list(map(lambda x: str(int(x)), arr.flatten())))
    # 紀錄inputcells長寬
    r, c = inputcells.shape
    # 對list中的每個set進行一系列操作，
    # 包含：取xy極值、紀錄那個block中1的位置(array)、儲存每個block的序列與左上角座標
    for i in list_:
        # xy極值
        xmin = max(min(j[0] for j in i) - 1, 0)
        xmax = min(max(j[0] for j in i) + 2, r+2)
        ymin = max(min(j[1] for j in i) - 1, 0)
        ymax = min(max(j[1] for j in i) + 2, c+2)
        # set轉換成array(擷取原始輸入)
        sq = np.zeros((r+2, c+2))
        sq[0:ymax-ymin, 0:xmax-xmin] = bigcellscopy[ymin:ymax,xmin:xmax]
        # array轉成str
        blocks.append((xmin + 1, ymin + 1, id(sq[1:-1, 1:-1])))
    return blocks

print(create_block(split(bigcells)))

# 序列的功能 ( i[2] for i in output )：
# 1.分析是否有消失／固定／震盪情況發生
# 2.加速龐大系統的計算時間