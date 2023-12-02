def input():
    with open("input2.txt") as f:
        lines = f.readlines()
    return lines

def split_input(lines):
    fish = []
    for i in lines :
        i = i.replace('\n', '')
        i = i.split(',')
        for j in i:
            j = int(j)
            fish.append(j)
    return fish

def one_day(fish):
    for i in range(len(fish)) :
        if fish[i] == 0 :
            fish.append(8)
            fish[i] = 6
        else :
            fish[i] -= 1
    return fish

def several_days(fish, nb_days):
    nb_1 = 0
    nb_2 = 0
    nb_3 = 0
    nb_4 = 0
    nb_5 = 0
    for i in range(nb_days):
        fish = one_day(fish)
        print("Day " + str(i + 1) + " : " + str(count_fish(fish)))
    # print(nb_1, nb_2, nb_3, nb_4, nb_5)
    return fish



def count_fish(fish):
    return len(fish)

def main():
    fish = split_input(input())
    print(count_fish(several_days(fish, 80)))
    fish = split_input(input())
    # print(count_fish(several_days(fish, 256)))


if __name__ == "__main__":
    main()

# 80 - 3 / 7 = 10,....

# 7 * x + 3 = 80
# 80 - 3 = 7x

# x = (80-3)/7 = 11

# 80 - 1 / 7 = 11