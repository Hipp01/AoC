def input():
    with open("input.txt") as f:
        lines = f.read()
    return lines[:-1]

def most_calories(lines):
    lines = lines.split("\n\n")
    elf = []
    calories = 0
    for i in lines:
        elf.append(i.split("\n"))
    for j in elf:
        cpt = 0
        for k in j:
            cpt += int(k)
        if cpt > calories:
            calories = cpt
    return calories

def second_most_calories(lines):
    most = most_calories(lines)
    lines = lines.split("\n\n")
    elf = []
    calories = 0
    for i in lines:
        elf.append(i.split("\n"))
    for j in elf:
        cpt = 0
        for k in j:
            cpt += int(k)
        if cpt > calories and cpt < most:
            calories = cpt
    return calories

def third_most_calories(lines):
    most = most_calories(lines)
    second = second_most_calories(lines)
    lines = lines.split("\n\n")
    elf = []
    calories = 0
    for i in lines:
        elf.append(i.split("\n"))
    for j in elf:
        cpt = 0
        for k in j:
            cpt += int(k)
        if cpt > calories and cpt < most and cpt < second:
            calories = cpt
    return calories
        
def main():
    lines = input()
    print(most_calories(lines))
    total_first_three = most_calories(lines) + second_most_calories(lines) + third_most_calories(lines)
    print(total_first_three)

if __name__ == "__main__":
    main()
