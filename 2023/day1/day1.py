def input():
    with open("input.txt") as f:
        lines = f.readlines()
    return lines


def calibration(lines):
    value = 0
    for line in lines:
        first, last = None, None
        for i in line:
            if i.isdigit():
                first = i
                break
        for j in reversed(line):
            if j.isdigit():
                last = j
                break
        if first is not None and last is not None:
            value += int(first + last)
    return value


def calibration_letters(lines):
    numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    value = 0
    for line in lines:
        first, last = None, None
        for i in range(len(line) + 1):
            if line[i].isdigit():
                first = line[i]
                break
            elif line[i:i + 3] in numbers.keys():
                first = numbers[line[i:i + 3]]
                break
            elif line[i:i + 4] in numbers.keys():
                first = numbers[line[i:i + 4]]
                break
            elif line[i:i + 5] in numbers.keys():
                first = numbers[line[i:i + 5]]
                break
        for j in range(-1, -len(line) - 1, -1):
            if line[j].isdigit():
                last = line[j]
                break
            elif line[j - 3:j] in numbers.keys():
                last = numbers[line[j - 3:j]]
                break
            elif line[j - 4: j] in numbers.keys():
                last = numbers[line[j - 4:j]]
                break
            elif line[j - 5: j] in numbers.keys():
                last = numbers[line[j - 5:j]]
                break
        if first is not None and last is not None:
            value += int(first + last)
    return value


def main():
    lines = input()
    # print(calibration(lines))
    print(calibration_letters(lines))


if __name__ == "__main__":
    main()
