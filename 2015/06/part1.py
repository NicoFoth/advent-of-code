with open("2015/Day6/input.txt") as inputFile:
    puzzleInput = inputFile.read().splitlines()


def partOne():
    grid = [[False for _ in range(1000)] for _ in range(1000)]
    for command in puzzleInput:
        if command.startswith("toggle"):
            cmd = command.split()[0]
            posOne = command.split()[1].split(",")
            posTwo = command.split()[3].split(",")
        else:
            cmd = command.split()[1]
            posOne = command.split()[2].split(",")
            posTwo = command.split()[4].split(",")

        for row in range(int(posOne[1]), int(posTwo[1])+1):
            for column in range(int(posOne[0]), int(posTwo[0])+1):
                if cmd == "on":
                    grid[row][column] = True
                elif cmd == "off":
                    grid[row][column] = False
                else:
                    if grid[row][column]:
                        grid[row][column] = False
                    else:
                        grid[row][column] = True
    counter = 0
    for row in grid:
        for column in row:
            if column:
                counter += 1
    print(counter)


partOne()