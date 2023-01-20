from collections import defaultdict


with open("2021/Day5/input.txt") as inputFile:
    input = [line for line in inputFile.read().splitlines()]


def partOne():
    environment = defaultdict(list)
    for path in input:
        complete_path = path
        path = path.split(" -> ")
        coord1 = path[0].split(",")
        coord2 = path[1].split(",")

        if not coord1[0] == coord2[0] and not coord1[1] == coord2[1]:
            continue

        path = [pos.split(",") for pos in path]
        for i in range(1):
            one = [int(x) for x in path[i]]
            two = [int(x) for x in path[i+1]]
            environment[tuple(one)].append(complete_path)
            for coord in range(2):
                for k in range(abs(one[coord]-two[coord])):
                    new = one.copy()
                    if two[coord] > one[coord]:
                        new[coord] += k+1
                    else:
                        new[coord] -= k+1
                    environment[tuple(new)].append(complete_path)

    counter = 0
    for key, value in environment.items():
        if len(value) >= 2:
            counter += 1

    print(counter)


partOne()