def input():
    with open("input.txt") as f:
        lines = f.readlines()
    return lines


def finger_position(lines):
    code = ''
    finger = 5
    for line in lines:
        for i in line:
            if i == 'R' and finger != 3 and finger != 6 and finger != 9:
                finger += 1
            elif i == 'L' and finger != 1 and finger != 4 and finger != 7:
                finger -= 1
            elif i == 'U' and finger != 1 and finger != 2 and finger != 3:
                finger -= 3
            elif i == 'D' and finger != 7 and finger != 8 and finger != 9:
                finger += 3
        code += str(finger)
    return code


def large_keypad(lines):
    code = ''
    finger = 5
    for line in lines:
        for i in line:
            if i == 'R' and finger != 1 and finger != 4 and finger != 9 and finger != 12 and finger != 13:
                finger += 1
            elif i == 'L' and finger != 1 and finger != 2 and finger != 5 and finger != 10 and finger != 13:
                finger -= 1
            elif i == 'U' and finger != 1 and finger != 2 and finger != 4 and finger != 5 and finger != 9:
                if finger == 3 or finger == 13:
                    finger -= 2
                else:
                    finger -= 4
            elif i == 'D' and finger != 5 and finger != 9 and finger != 10 and finger != 12 and finger != 13:
                if finger == 1 or finger == finger == 11:
                    finger += 2
                else:
                    finger += 4
        code += f'{finger:X}'
    return code


def main():
    lines = input()
    print(finger_position(lines))
    print(large_keypad(lines))


if __name__ == "__main__":
    main()
