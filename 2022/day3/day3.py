def input():
    with open("input.txt") as f:
        lines = f.read()
    return lines

def number_of_letter(letter):
    if letter.isalpha():
        if letter.isupper():
            return ord(letter) - 38
        else:
            return ord(letter) - 96
    else:
        return 0

def backpack(lines):
    lines = lines.split("\n")
    backpack = []
    for i in lines:
        backpack.append([i[0:len(i)//2], i[len(i)//2:]])
    return backpack


def repetition(one_backpack):
    set_1 = set(one_backpack[0])
    set_2 = set(one_backpack[1])
    resultat = list(set_1.intersection(set_2))
    return resultat


def priorities_sum(backpack):
    sum = 0
    for i in backpack:
        for j in repetition(i):
            sum += number_of_letter(j)
    return sum


def group_of_three(lines):
    lines = lines.split("\n")
    group = []
    for i in range(0, len(lines) - 2, 3):
        group.append([lines[i], lines[i+1], lines[i+2]])
    return group

def repetition_group(group):
    set_1 = set(group[0])
    set_2 = set(group[1])
    set_3 = set(group[2])
    resultat = list(set_1.intersection(set_2, set_3))
    return resultat

def priorities_sum_group(group):
    sum = 0
    for i in group:
        for j in repetition_group(i):
            sum += number_of_letter(j)
    return sum

def main():
    lines = input()
    print(priorities_sum(backpack(lines)))
    print(priorities_sum_group(group_of_three(lines)))


if __name__ == "__main__":
    main()