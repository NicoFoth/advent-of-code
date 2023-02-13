from itertools import groupby

with open("2015/Day10/input.txt", "r") as inputFile:
    input = inputFile.read().replace("\n", "")
    

def partOne():
    new_string = input
    for _ in range(40):
        new_string = "".join([str(len(list(iterator))) + char for char, iterator in groupby(new_string)])
    print(len(new_string))

partOne()