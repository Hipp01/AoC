from functools import reduce
from math import gcd
import re


def read_input():
    with open("input.txt") as f:
        lines = f.readlines()
    return lines


def follow_instructions(instructions, nodes):
    key = 'AAA'
    instructions *= 100
    cpt = 0
    while key != 'ZZZ':
        if instructions[0] == 'L':
            key = nodes[key][0]
        else:
            key = nodes[key][1]
        instructions = instructions[1:]
        cpt += 1
    return cpt


def calcul_ppcm(a, b):
    return a * b // gcd(a, b)


def ghost(instructions, nodes):
    tours = []
    instructions *= 1000
    keys = re.findall(r'\b\w{2}A\b', str(nodes.keys()))
    for key in keys:
        cpt = 0
        key2 = key
        i = instructions
        while key2[2] != 'Z':
            if i[0] == 'L':
                key2 = nodes[key2][0]
            else:
                key2 = nodes[key2][1]
            i = i[1:]
            cpt += 1
        tours.append(cpt)
    resultat = reduce(calcul_ppcm, tours)
    return resultat


def main():
    lines = read_input()
    instructions = lines[0].replace("\n", "")
    nodes = {node[:3]: [node[7:10], node[12:15]] for node in lines[2:]}
    print(follow_instructions(instructions, nodes))
    print(ghost(instructions, nodes))


if __name__ == "__main__":
    main()
