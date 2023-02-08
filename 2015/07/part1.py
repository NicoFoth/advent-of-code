with open("2015/Day7/input.txt", encoding="utf-8") as inputFile:
    input = inputFile.read().splitlines()
    definitions = {line.split(" -> ")[1]: line.split(" -> ")[0] for line in input}


def calculate(definition):
    operation = definitions[definition]
    if operation.isnumeric():
        return int(operation)
    
    operation = operation.split(" ")
    if len(operation) == 1:
        return calculate(operation[0])

    elif len(operation) == 2:
        return ~calculate(operation[1])

    if operation[1] == "AND":
        return calculate(operation[0]) & calculate(operation[2])
    elif operation[1] == "OR":
        return calculate(operation[0]) | calculate(operation[2])
    elif operation[1] == "XOR":
        return calculate(operation[0]) ^ calculate(operation[2])
    elif operation[1] == "LSHIFT":
        return calculate(operation[0]) << int(operation[2])
    elif operation[1] == "RSHIFT":
        return calculate(operation[0]) >> int(operation[2])

    


def partOne():
    result = calculate("h")
    print(result)


partOne()