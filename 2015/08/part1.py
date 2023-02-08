with open("2015/Day8/input.txt", encoding="utf-8") as inputFile:
    input = inputFile.read().splitlines()


def partOne():
    escaped_amount = 0
    unescaped_amount = 0
    for string in input:
        escaped_amount += len(eval(string))
    for string in input:
        unescaped_amount += len(string)
    
    result = unescaped_amount - escaped_amount
    print(result)


partOne()