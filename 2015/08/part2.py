with open("2015/Day8/input.txt", encoding="utf-8") as inputFile:
    input = inputFile.read().splitlines()


def partTwo():
    unescaped_amount = 0
    encoded_amount = 0
    for string in input:
        unescaped_amount += len(string)
        encoded_amount += len(string) + string.count("\"") + string.count("\\") + 2
    
    result = encoded_amount - unescaped_amount
    print(result)


partTwo()