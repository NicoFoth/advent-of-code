with open("2015/Day6/input.txt") as inputFile:
    input = inputFile.read().splitlines()


def partTwo():
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for command in input:
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
                    grid[row][column] += 1
                elif cmd == "off":
                    if grid[row][column] > 0:
                        grid[row][column] -= 1
                else:
                    grid[row][column] += 2
    counter = 0
    for row in grid:
        for column in row:
            counter += column
    print(counter)


partTwo()