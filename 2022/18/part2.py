from collections import defaultdict

with open("2022/Day18/input.txt") as inputFile:
    input = [tuple(int(y) for y in x.split(",")) for x in inputFile.read().splitlines()]


def partTwo():
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

    air_cubes = defaultdict(list)
    # Placing air cubes
    air_cube_placed_next_to_obsidian = True
    while air_cube_placed_next_to_obsidian:
        air_cube_placed_next_to_obsidian = False
        for cube in adjacent_cubes:
            if adjacent_cubes[cube] < 6:
                # Add air cube to air cubes on positions where a side of the cube is exposed to air
                # Also check if the cube currently looked at is obsidian to keep the while loop running
                pass
    
    # Remove air cubes if they are exposed to air until no cubes are removed

    # Count the unconnected sides of the obsidian cubes (input list)



partTwo()