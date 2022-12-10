with open("input.txt") as inputFile:
    input = inputFile.readlines()

    starting_position_input = []
    starting_position = [[] for i in range(9)]
    move_set = []
    for line in input:
        if line[0] == "m":
            move_set.append(line)
        else:
            starting_position_input.append(line)

    for line in starting_position_input:
        for index in range(len(line)):
            if line[index] == "[":
                if index % 4 == 0:
                    starting_position[index//4].append(line[index+1])


def one():
    solution = ""
    _starting_position = [x[:] for x in starting_position]
    for move in move_set:
        move_split = move.split()
        move_amount = int(move_split[1])
        pos1 = int(move_split[3])-1
        pos2 = int(move_split[5])-1

        for _ in range(move_amount):
            crate = _starting_position[pos1].pop(0)
            _starting_position[pos2].insert(0, crate)
    
    for stack in _starting_position:
        solution += stack[0]
    print(solution)


def two():
    solution = ""
    _starting_position = [x[:] for x in starting_position]
    for move in move_set:
        move_split = move.split()
        move_amount = int(move_split[1])
        pos1 = int(move_split[3])-1
        pos2 = int(move_split[5])-1

        crates = _starting_position[pos1][:move_amount]
        for _ in range(move_amount):
            _starting_position[pos1].pop(0)
        crates.reverse()
        for crate in crates:
            _starting_position[pos2].insert(0, crate)
    
    for stack in _starting_position:
        solution += stack[0]
    print(solution)


one()
two()