with open("2022/Day21/input.txt") as inputFile:
    input = inputFile.read().splitlines()
    definitions = {}
    for line in input:
        key, operation = line.split(": ")
        if operation.isnumeric():
            definitions[key] = int(operation)
        else:
            definitions[key] = operation.split(" ")


def calculate(definition):
    operation = definitions[definition]
    if isinstance(operation, int):
        return operation
    
    operation[0] = str(calculate(operation[0]))
    operation[2] = str(calculate(operation[2]))
    return eval("".join(operation))


def partOne():
    result = int(calculate("root"))
    print(result)
    



partOne()