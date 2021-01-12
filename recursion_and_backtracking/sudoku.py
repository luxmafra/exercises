import numpy as np

print("=====  S U D O K U  =====")
print("")
lst = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print(np.matrix(lst))
print("")
print("=====  SOLVED  ===== ")
print("")


def possible(y, x, n):
    global lst
    for i in range(0, 9):
        if lst[y][i] == n:
            return False
    for i in range(0, 9):
        if lst[i][x] == n:
            return False

    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if lst[y0+i][x0+j] == n:
                return False
    return True


def solve():
    global lst
    for y in range(9):
        for x in range(9):
            if lst[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        lst[y][x] = n
                        solve()
                        lst[y][x] = 0
                return
    print(np.matrix(lst))
    print("")
    input("More?")
    print("")


solve()
