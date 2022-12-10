with open("input.txt") as inputFile:
    input = inputFile.read().splitlines()


def one():
    head_x = 0
    head_y = 0
    tail_x = 0
    tail_y = 0
    tail_positions = []
    for line in input:
        direction = line.split()[0]
        steps = int(line.split()[1])

        for step in range(steps):

            # Move head
            if direction == "R":
                head_x += 1
            elif direction == "L":
                head_x -= 1
            elif direction == "U":
                head_y += 1
            else:
                head_y -= 1
            
            if not checkIfTouching([head_x, head_y], [tail_x, tail_y]):
                tail_x, tail_y = moveTail([head_x, head_y], [tail_x, tail_y])
            
            if [tail_x, tail_y] not in tail_positions:
                tail_positions.append([tail_x, tail_y])
    
    print(len(tail_positions))


def two():
    current_positions = [[0,0] for _ in range(10)]
    tail_positions = []
    for line in input:
        direction = line.split()[0]
        steps = int(line.split()[1])

        for step in range(steps):

            # Move head
            if direction == "R":
                current_positions[0][0] += 1
            elif direction == "L":
                current_positions[0][0] -= 1
            elif direction == "U":
                current_positions[0][1] += 1
            else:
                current_positions[0][1] -= 1

            for knot_index in range(1, len(current_positions)):
                if not checkIfTouching(current_positions[knot_index-1], current_positions[knot_index]):
                    current_positions[knot_index] = list(moveTail(current_positions[knot_index-1], current_positions[knot_index]))
            
            if current_positions[9] not in tail_positions:
                tail_positions.append(current_positions[9])

    print(len(tail_positions))
            


def checkIfTouching(head_pos, tail_pos):
    head_x = head_pos[0]
    head_y = head_pos[1]
    tail_x = tail_pos[0]
    tail_y = tail_pos[1]
    
    if abs(head_x - tail_x) <= 1:
        if abs(head_y - tail_y) <= 1:
            return True
        else:
            return False
    else:
        return False


def moveTail(head_pos, tail_pos):
    head_x = head_pos[0]
    head_y = head_pos[1]
    tail_x = tail_pos[0]
    tail_y = tail_pos[1]
    
    dist_x = abs(head_x - tail_x)
    dist_y = abs(head_y - tail_y)

    if dist_x == 0:
        if head_y > tail_y:
            tail_y += 1
        else:
            tail_y -= 1
    elif dist_y == 0:
        if head_x > tail_x:
            tail_x += 1
        else:
            tail_x -= 1
    else:
        if head_x > tail_x:
            tail_x += 1
        else:
            tail_x -= 1
        if head_y > tail_y:
            tail_y += 1
        else:
            tail_y -= 1
    return tail_x, tail_y
    


one()
two()