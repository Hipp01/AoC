import numpy as np


def input():
    with open("input.txt") as f:
        lines = f.readlines()
    return lines


def draw_rect(matrix, line):
    line = line.replace('\n', '').split(" ")
    x, y = map(int, line[1].split("x"))
    new_matrix = matrix.copy() if matrix is not None else np.zeros((6, 50), dtype=int)
    for i in range(x):
        for j in range(y):
            new_matrix[j][i] = 1
    return new_matrix


def rotate(matrix, line):
    line = line.replace('\n', '').split(" ")
    shift = int(line[-1])

    if line[1] == "row":
        row = int(line[2].split("=")[-1])
        new_matrix = matrix.copy() if matrix is not None else np.zeros((6, 50), dtype=int)
        new_matrix[row] = np.roll(matrix[row], shift)
    else:
        col = int(line[2].split("=")[-1])
        new_matrix = matrix.copy() if matrix is not None else np.zeros((6, 50), dtype=int)
        new_matrix[:, col] = np.roll(matrix[:, col], shift)

    return new_matrix


def main():
    lines = input()
    matrix = np.zeros((6, 50), dtype=int)
    for i in lines:
        if i.startswith("rect"):
            matrix = draw_rect(matrix, i)
        elif i.startswith("rotate"):
            matrix = rotate(matrix, i)
    print(np.sum(matrix))
    print(np.where(matrix == 0, '.', '#'))


if __name__ == "__main__":
    main()
