with open("input.txt") as inputFile:
    input = inputFile.readline()

def one():
    for i in range(3, len(input)):
        list = [input[i-index] for index in range(4)]
        if len(set(list)) == 4:
            print(i+1)
            break


def two():
    for i in range(13, len(input)):
        list = [input[i-index] for index in range(14)]
        if len(set(list)) == 14:
            print(i+1)
            break


one()
two()