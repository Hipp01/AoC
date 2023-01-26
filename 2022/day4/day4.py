def input():
    with open("input.txt") as f:
        lines = f.read()
    return lines

def split_by_pair(lines):
    lines = lines.split("\n")
    pair = []
    for i in lines[:-1]:
        i = i.split(",")
        pair.append([i[0], i[1]])
    return pair

def fully_contains(pair):
    elf_1 = pair[0].split("-")
    elf_2 = pair[1].split("-")
    if int(elf_1[0]) - int(elf_2[0]) <= 0 and int(elf_1[1]) - int(elf_2[1]) >= 0:
        return True
    elif int(elf_2[0]) - int(elf_1[0]) <= 0 and int(elf_2[1]) - int(elf_1[1]) >= 0:
        return True
    else:
        return False

def number_of_overlaps(lines):
    overlaps = 0
    for i in lines :
        if fully_contains(i):
            overlaps += 1
    return overlaps


def main():
    lines = input()
    print(number_of_overlaps(split_by_pair(lines)))


if __name__ == "__main__":
    main()