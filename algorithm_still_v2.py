import numpy as np
from tqdm import tqdm
from textwrap import wrap

with open("still_output_5.txt", "w") as file:
    file.write("Still cells\nInput cell size = 6 * 6\n")
database = set()
progress = tqdm(total = 2 ** 36 - 1)

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
            for array in (arr, arr.T, arr[::-1], arr[::-1].T, arr.T[::-1], arr.T[::-1].T, arr[::-1].T[::-1], arr[::-1].T[::-1].T):
                database.add("".join(array.astype(str).flatten()).strip("0").rstrip("0"))
            with open("still_output_5.txt", "a") as file:
                file.write("\n".join(i for i in wrap(strcell, 6) if i != "000000" and len(i) == 6) + "\n\n")
