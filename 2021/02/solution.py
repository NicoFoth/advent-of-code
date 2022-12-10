
file = open("input.txt", "r")

input_raw = file.readlines()

input = [x.strip("/n") for x in input_raw]

def partOne(input):
    depth = 0
    position = 0

    for command in input:
        command = command.split()
        if command[0] == "forward":
            position += int(command[1])
        elif command[0] == "up":
            depth -= int(command[1])
        elif command[0] == "down":
            depth += int(command[1])

    print(depth*position)

def partTwo(input):
    depth = 0
    position = 0
    aim = 0

    for command in input:
        command = command.split()
        if command[0] == "forward":
            position += int(command[1])
            depth += int(command[1]) * aim
        elif command[0] == "up":
            aim -= int(command[1])
        elif command[0] == "down":
            aim += int(command[1])

    print(depth*position)



partOne(input)
partTwo(input)