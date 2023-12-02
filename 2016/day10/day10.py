def input():
    with open("input.txt") as f:
        lines = f.read()
    return lines.replace('\n', '')




def main():
    lines = input()


if __name__ == "__main__":
    main()