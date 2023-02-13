from itertools import permutations

with open("2015/Day9/input.txt") as inputFile:
    input = inputFile.read().splitlines()
    locations = set()
    distances = dict()
    for line in input:
        source, _, destination, _, distance = line.split()
        locations.add(source)
        locations.add(destination)

        distances.setdefault(source, dict())[destination] = int(distance)
        distances.setdefault(destination, dict())[source] = int(distance)


def partTwo():
    solution = []
    
    for perm in permutations(locations):
        distance = sum(map(lambda x, y: distances[x][y], perm[:-1], perm[1:]))
        solution.append(distance)

    print(max(solution))


partTwo()