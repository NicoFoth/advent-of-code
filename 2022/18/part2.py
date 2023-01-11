from collections import deque

with open("2022/Day18/input.txt") as inputFile:
    input = [tuple(int(y) for y in x.split(",")) for x in inputFile.read().splitlines()]

all_cubes = set()
for cube in input:
    all_cubes.add(cube)
max_coord = max([max([cube[0] for cube in all_cubes]), max([cube[1] for cube in all_cubes]), max([cube[2] for cube in all_cubes])])
min_coord = min([min([cube[0] for cube in all_cubes]), min([cube[1] for cube in all_cubes]), min([cube[2] for cube in all_cubes])])


def getPositions(cube):
    possible_positions = [
        (cube[0]+1, cube[1], cube[2]),
        (cube[0]-1, cube[1], cube[2]),
        (cube[0], cube[1]+1, cube[2]),
        (cube[0], cube[1]-1, cube[2]),
        (cube[0], cube[1], cube[2]+1),
        (cube[0], cube[1], cube[2]-1),
    ]
    return possible_positions


def reaches_outside(cube):
    x, y, z = cube

    seen = set()
    queue = deque([(x,y,z)])

    while queue:
        x,y,z = queue.popleft()
        
        if (x,y,z) in all_cubes:
            continue
        if (x,y,z) in seen:
            continue
        
        seen.add((x,y,z))
        for coord in (x,y,z):
            if coord > max_coord or coord < min_coord:
                return True
        
        for adj in getPositions((x,y,z)):
            queue.append(adj)

    return False

def partTwo():
    surface_area = 0

    for (x,y,z) in all_cubes:
        if reaches_outside((x+1,y,z)):
            surface_area += 1
        if reaches_outside((x-1,y,z)):
            surface_area += 1
        if reaches_outside((x,y+1,z)):
            surface_area += 1
        if reaches_outside((x,y-1,z)):
            surface_area += 1
        if reaches_outside((x,y,z+1)):
            surface_area += 1
        if reaches_outside((x,y,z-1)):
            surface_area += 1
    
    print(surface_area)


partTwo()