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
    air_cube_placed_next_to_obsidian = True
    while air_cube_placed_next_to_obsidian:
        air_cube_placed_next_to_obsidian = False
        for cube in adjacent_cubes:
            if len(adjacent_cubes[cube]) < 6:
                # Find out which side is exposed to air (e.g. which positions)
                possible_positions = [
                    (cube[0]+1, cube[1], cube[2]),
                    (cube[0]-1, cube[1], cube[2]),
                    (cube[0], cube[1]+1, cube[2]),
                    (cube[0], cube[1]-1, cube[2]),
                    (cube[0], cube[1], cube[2]+1),
                    (cube[0], cube[1], cube[2]+1),
                ]
                # Also check if the cube currently looked at is obsidian to keep the while loop running
                for pos in possible_positions:
                    if pos in input:
                        air_cube_placed_next_to_obsidian = True
                
                exposed_positions = [x for x in possible_positions if x not in adjacent_cubes[cube]]
                

                # Add air cube to air cubes on positions where a side of the cube is exposed to air
                for pos in exposed_positions:
                    adjacent_cubes[cube].append(pos)
                    air_cubes[pos] = [x for x in possible_positions if x in adjacent_cubes]
        for key, value in air_cubes.items():
            adjacent_cubes[key] = value
                
    
    # Remove air cubes if they are exposed to air until no cubes are removed
    removed = True
    while removed:
        removed = False
        to_be_removed = []
        for cube in adjacent_cubes:
            if cube in input:
                continue
            for adj_cube in adjacent_cubes[cube]:
                if adj_cube in input:
                    break
            else:
                possible_positions = [
                    (cube[0]+1, cube[1], cube[2]),
                    (cube[0]-1, cube[1], cube[2]),
                    (cube[0], cube[1]+1, cube[2]),
                    (cube[0], cube[1]-1, cube[2]),
                    (cube[0], cube[1], cube[2]+1),
                    (cube[0], cube[1], cube[2]+1),
                    ]
                if [x for x in possible_positions if x not in adjacent_cubes[cube]]:
                    to_be_removed.append(cube)
        if to_be_removed:
            removed = True
        for deletion in to_be_removed:
            adjacent_cubes.pop(deletion)
            for cube in adjacent_cubes:
                if deletion in adjacent_cubes[cube]:
                    adjacent_cubes[cube].remove(deletion)


    # Count the unconnected sides of the obsidian cubes (input list)
    for cube in adjacent_cubes:
        if cube in adjacent_cubes:
            unconnected_sides += 6-len(adjacent_cubes[cube])
        else:
            unconnected_sides += 6
    print(unconnected_sides)


partTwo()