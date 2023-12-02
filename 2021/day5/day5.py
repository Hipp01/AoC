import numpy as np

def input():
    with open("input.txt") as f:
        lines = f.readlines()
    return lines

def split_coord(lines):
    coord = []
    for i in lines:
        i = i.replace(' -> ', ',')
        i = i.replace('\n', '')
        coord.append(i.split(','))
    return coord

def grid(nb_lines, nb_columns):
    return np.zeros((nb_lines, nb_columns))

def fill_grid(grid, coord):
    a = np.array(grid)
    for i in coord:
        x1 = int(i[0])
        y1 = int(i[1])
        x2 = int(i[2])
        y2 = int(i[3])
        if x1 == x2 :
            for j in range(min(y1, y2), max(y1, y2) + 1):
                a[x1][j] += 1
        elif y1 == y2 :
            for j in range(min(x1, x2), max(x1, x2) + 1):
                a[j][y1] += 1
    return np.transpose(a)

def fill_grid_diagonal(grid, coord):
    a = np.array(grid)
    for i in coord:
        x1 = int(i[0])
        y1 = int(i[1])
        x2 = int(i[2])
        y2 = int(i[3])
        if x1 > x2 and y1 > y2:
            for j in range(x1 - x2 + 1):
                a[x1 - j][y1 - j] += 1
        elif x1 > x2 and y1 < y2:
            for j in range(x1 - x2 + 1):
                a[x1 - j][y1 + j] += 1
        elif x1 < x2 and y1 > y2:
            for j in range(x2 - x1 + 1):
                a[x1 + j][y1 - j] += 1
        elif x1 < x2 and y1 < y2:
            for j in range(x2 - x1 + 1):
                a[x1 + j][y1 + j] += 1
    return np.transpose(a)

def count_grid(grid):
    return np.count_nonzero(grid > 1)

def merge_grid(grid1, grid2):
    return grid1 + grid2

def main():
    coord = split_coord(input())
    grid_filled = fill_grid(grid(1000, 1000), coord)
    # print(grid_filled)
    # print('\n----------------\n')
    print(count_grid(grid_filled))
    # print('\n----------------\n')
    grid_diagonal = fill_grid_diagonal(grid(1000, 1000), coord)
    # print(grid_diagonal)
    # print(count_grid(grid_diagonal))
    # print('\n----------------\n')
    # print(merge_grid(grid_filled, grid_diagonal))
    grid_merged = merge_grid(grid_filled, grid_diagonal)
    print(count_grid(grid_merged))

if __name__ == "__main__":
    main()