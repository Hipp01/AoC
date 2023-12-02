def input():
    with open("input.txt") as f:
        lines = f.read()
    return lines


def compass(direction, command):
    if direction == 'N':
        if command == 'R':
            return 'E'
        elif command == 'L':
            return 'W'
    elif direction == 'E':
        if command == 'R':
            return 'S'
        elif command == 'L':
            return 'N'
    elif direction == 'S':
        if command == 'R':
            return 'W'
        elif command == 'L':
            return 'E'
    elif direction == 'W':
        if command == 'R':
            return 'N'
        elif command == 'L':
            return 'S'


def move(direction, distance, x, y):
    if direction == 'N':
        y += distance
    elif direction == 'E':
        x += distance
    elif direction == 'S':
        y -= distance
    elif direction == 'W':
        x -= distance
    return x, y


def blocks_away(lines):
    direction = 'N'
    x = 0
    y = 0
    for line in lines:
        command = line[0]
        distance = int(line[1:])
        direction = compass(direction, command)
        x, y = move(direction, distance, x, y)
    return abs(x) + abs(y)


def already_visited(x, y, visited):
    for i in visited:
        if i[0] == x and i[1] == y:
            return abs(x) + abs(y)
    return 0


def visit(lines):
    direction = 'N'
    x = 0
    y = 0
    visited = []
    for line in lines:
        command = line[0]
        distance = int(line[1:])
        direction = compass(direction, command)
        for i in range(distance):
            x, y = move(direction, 1, x, y)
            if already_visited(x, y, visited) != 0:
                return already_visited(x, y, visited)
            visited.append((x, y))
    return 0


def main():
    lines = input()
    lines = lines.replace('\n', '').split(', ')
    print(blocks_away(lines))
    print(visit(lines))


if __name__ == "__main__":
    main()
