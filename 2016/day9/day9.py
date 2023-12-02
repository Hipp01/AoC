import re


def input():
    with open("input.txt") as f:
        lines = f.read()
    return lines.replace('\n', '')


def decompress(lines):
    final_string = ''
    i = 0
    while i != len(lines):
        numbers = ''
        if lines[i] == '(':
            i += 1
            while lines[i] != ')':
                numbers += lines[i]
                i += 1
            first = int(numbers.split('x')[0])
            second = int(numbers.split('x')[1])
            final_string += lines[i + 1:i + 1 + first] * second
            i += 1 + first
        else:
            final_string += lines[i]
            i += 1
    return len(final_string)


def decompressed_length(s):
    i = 0
    length = 0

    while i < len(s):
        if s[i] == '(':
            match = re.match(r'\((\d+)x(\d+)\)', s[i:])
            if match:
                n, m = map(int, match.groups())
                i += match.end()
                substring = s[i:i + n]
                length += decompressed_length(substring) * m
                i += n
            else:
                length += 1
                i += 1
        else:
            length += 1
            i += 1

    return length


def main():
    lines = input()
    print(decompress(lines))
    print(decompressed_length(lines))


if __name__ == "__main__":
    main()
