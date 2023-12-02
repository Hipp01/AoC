def input():
    with open("input.txt") as f:
        lines = f.readlines()
    return lines


def real_room(line):
    code = line.split('-')[-1].split('[')[0]
    alphabet = line.split('-')[-1].split('[')[1][:-2]
    letters = ''.join(line.split('-')[:-1])
    letters_sorted = sorted(letters)
    letters_sorted = ''.join(sorted(letters_sorted, key=letters.count, reverse=True))
    unique_letters = ''
    for j in letters_sorted:
        if j not in unique_letters:
            unique_letters += j
    if unique_letters[:len(alphabet)] == alphabet:
        return int(code), letters
    return 0, ''


def decrypt(code, letters):
    return ''.join([chr(((ord(c) - 65 + code) % 26) + 65) if c.isupper() else chr(((ord(c) - 97 + code) % 26) + 97) if c.islower() else c for c in letters])


def main():
    lines = input()
    cpt = 0
    for i in lines:
        room = real_room(i)
        code = room[0]
        letters = room[1]
        cpt += code
        if letters != '':
            if decrypt(code, letters) == "northpoleobjectstorage":
                objects = code
    print(cpt)
    print(objects)


if __name__ == "__main__":
    main()
