with open("2015/Day9/input.txt") as inputFile:
    input = inputFile.read().splitlines()
    distances = [int(x.split("= ")[1]) for x in input]


def partOne():
    distance_combinations = []
    for x in range(len(distances)):
        for y in range(x+1, len(distances)):
            distance_combinations.append(distances[x]+distances[y])
    print(min(distance_combinations))

partOne()