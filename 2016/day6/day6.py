def input():
    with open("input.txt") as f:
        lines = f.readlines()
    return lines


def more_present(lines):
    repetitions = []
    for i in range(len(lines[0])):
        letters = {}
        for line in lines:
            letter = line[i].strip()
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        repetitions.append(sorted(letters.items(), key=lambda x: x[1], reverse=True)[0][0])
    return "".join(repetitions)


def less_present(lines):
    repetitions = []
    for i in range(len(lines[0])):
        letters = {}
        for line in lines:
            letter = line[i].strip()
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        repetitions.append(sorted(letters.items(), key=lambda x: x[1])[0][0])
    return "".join(repetitions)


def main():
    lines = input()
    print(more_present(lines))
    print(less_present(lines))


if __name__ == "__main__":
    main()
