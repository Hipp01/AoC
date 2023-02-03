def input():
    with open("input.txt") as f:
        lines = f.read()
    return lines


def first_marker_4(lines):
    for i in range(4, len(lines)):
        last4markers = set()
        last4markers.add(lines[i-4])
        last4markers.add(lines[i-3])
        last4markers.add(lines[i-2])
        last4markers.add(lines[i-1])
        if len(last4markers) == 4:
            return i
    return -1


def first_marker_14(lines):
    for i in range(14, len(lines)):
        last14markers = set()
        last14markers.add(lines[i-14])
        last14markers.add(lines[i-13])
        last14markers.add(lines[i-12])
        last14markers.add(lines[i-11])
        last14markers.add(lines[i-10])
        last14markers.add(lines[i-9])
        last14markers.add(lines[i-8])
        last14markers.add(lines[i-7])
        last14markers.add(lines[i-6])
        last14markers.add(lines[i-5])
        last14markers.add(lines[i-4])
        last14markers.add(lines[i-3])
        last14markers.add(lines[i-2])
        last14markers.add(lines[i-1])
        if len(last14markers) == 14:
            return i
    return -1


def main():
    lines = input()
    print(first_marker_4(lines))
    print(first_marker_14(lines))


if __name__ == "__main__":
    main()
