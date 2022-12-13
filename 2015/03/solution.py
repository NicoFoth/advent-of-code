with open("2015/Day3/input.txt") as inputFile:
    input = inputFile.read()


def partOne():
    houses_visited = []
    current_position = [0, 0]
    for direction in input:
        if current_position not in houses_visited:
            houses_visited.append(current_position.copy())
        
        if direction == "^":
            current_position[1] += 1
        elif direction == "v":
            current_position[1] -= 1
        elif direction == "<":
            current_position[0] -= 1
        else:
            current_position[0] += 1
    print(len(houses_visited))


def partTwo():
    houses_visited = []
    current_positions = [[0, 0], [0, 0]]
    for direction_index in range(0, len(input), 2):
        
        for i in range(2):
            if current_positions[i] not in houses_visited:
                houses_visited.append(current_positions[i].copy())

            if input[direction_index+i] == "^":
                current_positions[i][1] += 1
            elif input[direction_index+i] == "v":
                current_positions[i][1] -= 1
            elif input[direction_index+i] == "<":
                current_positions[i][0] -= 1
            else:
                current_positions[i][0] += 1
    print(len(houses_visited))


partOne()
partTwo()