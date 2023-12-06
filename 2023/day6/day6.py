def input():
    with open("input.txt") as f:
        lines = f.readlines()
    return lines


def races(lines):
    times = lines[0].split()[1:]
    distances = lines[1].split()[1:]
    total = 1
    for i in range(len(times)):
        victories = 0
        for j in range(int(times[i]) + 1):
            if int(distances[i]) < j * (int(times[i]) - j):
                victories += 1
        total *= victories
    return total


def only_one_race(lines):
    time = lines[0].replace("Time: ", "")
    distance = lines[1].replace("Distance: ", "")
    while " " in time or " " in distance:
        time = time.replace(" ", "")
        distance = distance.replace(" ", "")
    time = int(time)
    distance = int(distance)
    victories = 0
    for i in range(time + 1):
        if distance < i * (time - i):
            victories += 1
    return victories


def main():
    lines = input()
    print(races(lines))
    print(only_one_race(lines))


if __name__ == "__main__":
    main()
