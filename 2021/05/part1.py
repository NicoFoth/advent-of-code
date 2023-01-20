from collections import defaultdict


with open("2021/Day5/input.txt") as inputFile:
    input = [line for line in inputFile.read().splitlines()]


def partOne():
    environment = defaultdict(list)
    for path in input:
        complete_path = path
        path = path.split(" -> ")
        path = [pos.split(",") for pos in path]
        one = [int(x) for x in path[0]]
        two = [int(x) for x in path[1]]

        if not one[0] == two[0] and not one[1] == two[1]:
            continue

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