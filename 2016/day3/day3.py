def input():
    with open("input.txt") as f:
        lines = f.readlines()
    return lines


def possible_triangles(lines):
    cpt = 0
    for i in lines:
        liste = i.replace('    ', '  ').replace('   ', '  ').replace('\n', '').split('  ')[1:]
        mini, maxi = min(int(liste[0]), int(liste[1]), int(liste[2])), max(int(liste[0]), int(liste[1]), int(liste[2]))
        liste.remove(str(mini))
        liste.remove(str(maxi))
        other = int(liste[0])
        if mini + other > maxi:
            cpt += 1
    return cpt


def possible_triangles_columns(lines):
    cpt = 0
    for i in range(0, len(lines), 3):
        for j in range(4):
            sides = [lines[i + k].replace('    ', '  ').replace('   ', '  ').replace('\n', '').split('  ')[j] for k in range(3)
                     if lines[i + k].replace('    ', '  ').replace('   ', '  ').replace('\n', '').split('  ')[j].strip().isdigit()]
            sides = [int(side) for side in sides]
            if len(sides) == 3:
                mini, maxi = min(sides), max(sides)
                sides.remove(mini)
                sides.remove(maxi)
                other = sides[0]
                if mini + other > maxi:
                    cpt += 1

    return cpt


def main():
    lines = input()
    print(possible_triangles(lines))
    print(possible_triangles_columns(lines))


if __name__ == "__main__":
    main()
