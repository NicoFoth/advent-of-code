with open("2022/Day24/input.txt") as inputFile:
    input = [list(line) for line in inputFile.read().splitlines()]


def getNextPlayerPositions(possiblePositions, grid, new_blizzards):
    moves = ((1,0), (-1,0), (0,1), (0,-1), (0,0))
    possible_next_moves = set()
    for possiblePos in possiblePositions:
        for move in moves:
            temp = list(possiblePos)
            for i in range(len(move)):
                temp[i] += move[i]
            if not (0 <= temp[0] <= len(grid)-1 and 0 <= temp[1] <= len(grid[1])-1):
                continue
            for move in moves:
                tempset = set()
                tempset.add((move, tuple(temp)))
                if tempset.issubset(new_blizzards):
                    break
            else:
                if grid[temp[0]][temp[1]] == ".":
                    possible_next_moves.add(tuple(temp))
    return possible_next_moves


def solveBFS(end, grid, blizzards, minutes, possiblePositions):
    while end not in possiblePositions:

        new_blizzards = set()
        for blizzard in blizzards:
            direction, current_pos = blizzard
            new_pos = list(current_pos)

            new_pos[0] += direction[0]
            new_pos[1] += direction[1]
            if 0 < new_pos[0] < len(grid)-1 and 0 < new_pos[1] < len(grid[new_pos[0]])-1:
                new_blizzards.add((direction, tuple(new_pos)))
            else:
                if direction == (0, -1):
                    new_blizzards.add((direction, (current_pos[0], len(grid[current_pos[0]])-2)))
                elif direction == (0, 1):
                    new_blizzards.add((direction, (current_pos[0], 1)))
                elif direction == (-1, 0):
                    new_blizzards.add((direction, (len(grid)-2, current_pos[1])))
                elif direction == (1, 0):
                    new_blizzards.add((direction, (1, current_pos[1])))

        possiblePositions = getNextPlayerPositions(possiblePositions, grid, new_blizzards)
        
        blizzards = new_blizzards
        minutes += 1

    return minutes, blizzards



def partTwo():
    grid = input.copy()
    for char_index in range(len(grid[0])):
        if grid[0][char_index] == ".":
            start = (0, char_index)
    for char_index in range(len(grid[-1])):
        if grid[-1][char_index] == ".":
            end = (len(grid)-1, char_index)

    possiblePositionsStart = set()
    possiblePositionsStart.add(start)
    possiblePositionsEnd = set()
    possiblePositionsEnd.add(end)

    blizzards = set()
    for row_index in range(len(grid)):
        for char_index in range(len(grid[row_index])):
            if grid[row_index][char_index] == "<":
                blizzards.add(((0, -1), (row_index, char_index)))
                grid[row_index][char_index] = "."
            elif grid[row_index][char_index] == ">":
                blizzards.add(((0, 1), (row_index, char_index)))
                grid[row_index][char_index] = "."
            elif grid[row_index][char_index] == "v":
                blizzards.add(((1, 0), (row_index, char_index)))
                grid[row_index][char_index] = "."
            elif grid[row_index][char_index] == "^":
                blizzards.add(((-1, 0), (row_index, char_index)))
                grid[row_index][char_index] = "."
    
    minutes1, blizzards1 = solveBFS(end, grid, blizzards, 0, possiblePositionsStart)
    minutes2, blizzards2 = solveBFS(start, grid, blizzards1, 0, possiblePositionsEnd)
    minutes3, _ = solveBFS(end, grid, blizzards2, 0, possiblePositionsStart)

    print(sum([minutes1, minutes2, minutes3]))

partTwo()