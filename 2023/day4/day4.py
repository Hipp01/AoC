def input():
    with open("input.txt") as f:
        lines = f.readlines()
    return lines


def winning_cards(line):
    cpt = 0
    winning_numbers = line.split(" | ")[0].replace('  ', ' ').split(": ")[1].split(" ")
    cards = line.split(" | ")[1].replace('\n', '').replace('  ', ' ').split(' ')
    for card in cards:
        if card in winning_numbers:
            cpt += 1
    return cpt


def total_points(lines):
    total = 0
    for line in lines:
        total += 2**(winning_cards(line) - 1) if winning_cards(line) > 0 else 0
    return total


def total_scratchcards(lines):
    cards = {}
    cpt = 0
    for i in range(1, len(lines) + 1):
        cards[i] = 1
    for line in range(len(lines)):
        for j in range(1, winning_cards(lines[line]) + 1):
            cards[line + j + 1] += cards[line + 1]
    for i in cards.values():
        cpt += i
    return cpt


def main():
    lines = input()
    print(total_points(lines))
    print(total_scratchcards(lines))


if __name__ == "__main__":
    main()
