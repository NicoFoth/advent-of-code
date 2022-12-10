with open("input.txt") as inputFile:
    input = inputFile.read().splitlines()


def one():
    filesystem = {"/": []}
    for line in input:
        if line[0] == "$":
            line_split = line.split()
            command = line_split[1]
            if command == "cd":
                argument = line_split[2]
            