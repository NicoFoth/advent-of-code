from collections import defaultdict

with open("2022/Day18/input.txt") as inputFile:
    input = [tuple(int(y) for y in x.split(",")) for x in inputFile.read().splitlines()]


def partOne():
    adjacent_cubes = defaultdict(list)
    unconnected_sides = 0
    for cube in input:
        for cube2 in input:
            if cube == cube2:
                continue
            if abs(cube[0]-cube2[0]) == 1 and cube[1] == cube2[1] and cube[2] == cube2[2]:
                adjacent_cubes[cube].append(cube2)
            elif abs(cube[1]-cube2[1]) == 1 and cube[0] == cube2[0] and cube[2] == cube2[2]:
                adjacent_cubes[cube].append(cube2)
            elif abs(cube[2]-cube2[2]) == 1 and cube[0] == cube2[0] and cube[1] == cube2[1]:
                adjacent_cubes[cube].append(cube2)
        if cube in adjacent_cubes:
            unconnected_sides += 6-len(adjacent_cubes[cube])
        else:
            unconnected_sides += 6

    print(unconnected_sides)
            

partOne()