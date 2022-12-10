with open("input.txt") as inputFile:
        input = inputFile.readlines()

def one():
    total_score = 0
    values = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    beats = {1: 3, 2: 1, 3: 2}

    for line in input:
        opponents_move = values[line.split()[0]]
        own_move = values[line.split()[1]]
        
        if own_move == opponents_move:
            total_score += own_move+3

        elif beats[own_move] == opponents_move:
            total_score += own_move+6
        else:
            total_score += own_move

    print(total_score)


def two():
    total_score = 0
    values = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    beats = {1: 3, 2: 1, 3: 2}

    for line in input:
        opponents_move = values[line.split()[0]]
        outcome = values[line.split()[1]]

        if outcome == 1:
            total_score += beats[opponents_move]
        elif outcome == 2:
            total_score += opponents_move+3
        else:
            total_score += beats[beats[opponents_move]]+6

    print(total_score)

one()
two()