with open("2015/Day1/input.txt") as inputFile:
    input = inputFile.read()


def one():
    current_floor = 0
    for char in input:
        if char == "(":
            current_floor += 1
        else:
            current_floor -= 1
    print(current_floor)


def two():
    current_floor = 0
    for char_index in range(len(input)):
        if input[char_index] == "(":
            current_floor += 1
        else:
            current_floor -= 1
        if current_floor < 0:
            print(char_index+1)
            break

one()
two()