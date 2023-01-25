with open("2022/Day21/input.txt") as inputFile:
    input = inputFile.read().splitlines()
    definitions = {}
    for line in input:
        key, operation = line.split(": ")
        if operation.isnumeric():
            definitions[key] = int(operation)
        else:
            definitions[key] = tuple(operation.split(" "))


def calculate(definition):
    if definition == "humn":
        return False
    operation = definitions[definition]
    if isinstance(operation, int):
        return operation
    operation = list(operation)
    if operation[1] == "/":
        operation[1] = "//"
    
    operation[0] = str(calculate(operation[0]))
    operation[2] = str(calculate(operation[2]))
    if operation[0] == "False" or operation[2] == "False":
        return False
    
    return eval("".join(operation))


def calculateBackwards(definition, result):
    if definition == "humn":
        return result
    operators = {"+": "-", "-": "+", "*": "//", "/": "*"}
    operation = list(definitions[definition])
    var1 = calculate(operation[0])
    var2 = calculate(operation[2])
    next_result = 0

    if not var1:
        next_result = eval("".join([str(result), operators[operation[1]], str(var2)]))
        return calculateBackwards(operation[0], next_result)
    else:
        if operation[1] == "-" or operation[1] == "/":
            next_result = eval("".join([str(var1), operation[1], str(result)]))
        else:
            next_result = eval("".join([str(result), operators[operation[1]], str(var1)]))
        return calculateBackwards(operation[2], next_result)


def partTwo():
    operation = definitions["root"]
    var1 = calculate(operation[0])
    var2 = calculate(operation[2])


    if not var1:
        solution = int(calculateBackwards(operation[0], var2))
    else:
        solution = int(calculateBackwards(operation[2], var1))

    print(solution)
    

partTwo()