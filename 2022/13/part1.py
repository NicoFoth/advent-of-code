with open("2022/Day13/input.txt") as inputFile:
    input = inputFile.read().splitlines()

    pairs = [[eval(input[line_index-2]), eval(input[line_index-1])] for line_index in range(len(input)) if input[line_index] == ""]


def listChecker(list1, list2):
    for element1, element2 in zip(list1, list2):
        if type(element1) == int and type(element2) == int:
            if element1 == element2:
                pass
            elif element1 < element2:
                return True
            else:
                return False
        
        elif type(element1) == list and type(element2) == list:
            res = listChecker(element1, element2)
            if res != None:
                return res
        
        else:
            if type(element1) == list:
                res = listChecker(element1, [element2])
            else:
                res = listChecker([element1], element2)
            if res != None:
                return res
    
    else:
        if len(list1) == len(list2):
            return None
        elif len(list1) < len(list2):
            return True
        else:
            return False


def partOne():
    indices_sum = 0
    for pair, index in zip(pairs, range(1, len(pairs)+1)):
        if listChecker(pair[0], pair[1]):
            indices_sum += index
    print(indices_sum)

partOne()