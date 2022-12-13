with open("2015/Day2/input.txt") as inputFile:
    input = inputFile.read().splitlines()


def partOne():
    overall_area = 0
    for box in input:
        x = [int(x) for x in box.split("x")]
        x.sort()
        length, width, height = x
        overall_area += 3*length*width + 2*length*height + 2*width*height
    print(overall_area)


def partTwo():
    overall_length = 0
    for box in input:
        x = [int(x) for x in box.split("x")]
        x.sort()
        length, width, height = x
        overall_length += 2*length + 2*width + length*width*height
    print(overall_length)


partOne()
partTwo()