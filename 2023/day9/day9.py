def read_input():
    with open("input.txt") as f:
        return f.readlines()


def extrapolate(lines):
    res = 0
    for line in lines:
        numbers = [int(x) for x in line.strip().split()]
        last_digits = numbers[-1]
        while True:
            differences = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
            last_digits += differences[-1]
            if all(x == differences[0] for x in differences):
                res += last_digits
                break
            numbers = differences
    return res


def extrapolate_backwards(lines):
    res = 0
    for line in lines:
        numbers = [int(x) for x in line.strip().split()]
        found = False
        first_digit = numbers[0]
        difference_of_differences = 0
        idx = 0
        while not found:
            differences = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
            if idx % 2 == 0:
                difference_of_differences += differences[0]
            else:
                difference_of_differences -= differences[0]
            if all(x == differences[0] for x in differences):
                found = True
                res += (first_digit - difference_of_differences)
            idx += 1
            numbers = differences
    return res


def main():
    lines = read_input()
    # print(extrapolate(lines))
    print(extrapolate_backwards(lines))


if __name__ == '__main__':
    main()
