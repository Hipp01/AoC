def input():
    with open("input.txt") as f:
        lines = f.readlines()
    return lines


def possible_game(line):
    id = line.split(':')[0].split(' ')[1]
    game = line.replace('\n', '').replace(';', ',').replace('Game ' + id + ': ', '').split(', ')
    for i in game:
        n = int(i.split()[0])
        color = i.split()[1]
        if (n > 12 and color == "red") or (n > 13 and color == "green") or (n > 14 and color == "blue"):
            return 0
    return int(id)


def count_games(lines):
    cpt = 0
    for line in lines:
        cpt += possible_game(line)
    return cpt


def power(lines):
    cpt = 0
    for line in lines:
        red, green, blue = 0, 0, 0
        id = line.split(':')[0].split(' ')[1]
        game = line.replace('\n', '').replace(';', ',').replace('Game ' + id + ': ', '').split(', ')
        for i in game:
            number = int(i.split()[0])
            color = i.split()[1]
            if color == "red" and number > red:
                red = number
            elif color == "green" and number > green:
                green = number
            if color == "blue" and number > blue:
                blue = number
        cpt += red * green * blue
    return cpt


def main():
    lines = input()
    print(count_games(lines))
    print(power(lines))


if __name__ == "__main__":
    main()
