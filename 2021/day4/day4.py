import numpy as np

def input():
    with open("input.txt") as f:
        lines = f.readlines()
    return lines

def bingo():
    lines = input()
    numeros = lines[0].split(',')
    tableau = np.array(5*[5*[0]])
    return tableau




if __name__=="__main__":
    print(bingo())