def input():
    with open("input.txt") as f:
        lines = f.read()
    return lines


def crates(lines):
    lines = lines.split("\n")[0:8]
    crate_1, crate_2, crate_3, crate_4, crate_5, crate_6, crate_7, crate_8, crate_9 = [], [], [], [], [], [], [], [], []
    for i in lines:
        i = i.replace("    ", "[]")
        i = i.replace(" ", "")
        i = i[1:-1].split("][")
        crate_1.append(i[0])
        crate_2.append(i[1])
        crate_3.append(i[2])
        crate_4.append(i[3])
        crate_5.append(i[4])
        crate_6.append(i[5])
        crate_7.append(i[6])
        crate_8.append(i[7])
        crate_9.append(i[8])
    crates = [crate_1, crate_2, crate_3, crate_4, crate_5, crate_6, crate_7, crate_8, crate_9]
    for i in crates:
        while "" in i:
            i.remove("")
        i.reverse()
    return crates


def movments(lines):
    lines = lines.split("\n")[10:]
    movments = []
    for i in lines[:-1]:
        i = i[5:].split()
        movments.append([int(i[0]), int(i[2]), int(i[4])])
    return movments


def move(movment, crates):
    for i in movment:
        crate_start = crates[i[1] - 1]
        crate_end = crates[i[2] - 1]
        for j in range(i[0]):
            crate_end += crate_start.pop()
    return crates


def move_2(movment, crates):
    for i in movment:
        crate_start = crates[i[1] - 1]
        crate_end = crates[i[2] - 1]
        temp = []
        for j in range(i[0]):
            temp.append(crate_start.pop())
        temp.reverse()
        for j in temp:
            crate_end.append(j)
    return crates


def final_word(crates):
    word = ""
    for i in crates:
        word += i[-1]
    return word


def main():
    lines = input()
    print(final_word(move(movments(lines), crates(lines))))
    print(final_word(move_2(movments(lines), crates(lines))))


if __name__ == "__main__":
    main()
