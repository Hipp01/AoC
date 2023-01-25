def input():
    with open("input.txt") as f:
        lines = f.read()
    return lines[:-1]

input_test = "A Y\nB \nC Z"

def win(player1, player2):
    if player1 == "A" and player2 == "X":
        return 0
    elif player1 == "A" and player2 == "Y":
        return 2
    elif player1 == "A" and player2 == "Z":
        return 1
    elif player1 == "B" and player2 == "X":
        return 1
    elif player1 == "B" and player2 == "Y":
        return 0
    elif player1 == "B" and player2 == "Z":
        return 2
    elif player1 == "C" and player2 == "X":
        return 2
    elif player1 == "C" and player2 == "Y":
        return 1
    elif player1 == "C" and player2 == "Z":
        return 0


def points(round):
    round = round.split(" ")
    player1 = round[0]
    player2 = round[1]
    winner = win(player1, player2)
    shape = player2
    if shape == "X":
        round_points = 1
    elif shape == "Y":
        round_points = 2
    elif shape == "Z":
        round_points = 3

    if winner == 0:
        round_points += 3
    elif winner == 1:
        round_points += 0
    elif winner == 2:
        round_points += 6
    return round_points

def tournament(lines):
    lines = lines.split("\n")
    cpt = 0
    for i in lines:
        cpt += points(i)
    return cpt


def points_second_strategy(round):
    round = round.split(" ")
    player1 = round[0]
    player2 = round[1]
    if player2 == "X":
        round_points = 0
        if player1 == "A":
            round_points += 3
        elif player1 == "B":
            round_points += 1
        elif player1 == "C":
            round_points += 2
    elif player2 == "Y":
        round_points = 3
        if player1 == "A":
            round_points += 1
        elif player1 == "B":
            round_points += 2
        elif player1 == "C":
            round_points += 3
    elif player2 == "Z":
        round_points = 6
        if player1 == "A":
            round_points += 2
        elif player1 == "B":
            round_points += 3
        elif player1 == "C":
            round_points += 1
    return round_points

def tournament_second_strategy(lines):
    lines = lines.split("\n")
    cpt = 0
    for i in lines:
        cpt += points_second_strategy(i)
    return cpt

def main():
    lines = input()
    print(tournament(lines))
    print(tournament_second_strategy(lines))


if __name__ == "__main__":
    main()