from copy import deepcopy


with open("2022/Day13/input.txt") as inputFile:
    input = inputFile.read().splitlines()

    input = [eval(input[line_index]) for line_index in range(len(input)) if input[line_index] != ""]

sorted = []
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


def partTwo():
    sorted = deepcopy(input)
    sorted.append([[2]])
    sorted.append([[6]])
    for iteration in range(len(sorted)):
        for index in range(len(sorted)-1):
            if not listChecker(sorted[index], sorted[index+1]):
                sorted.insert(index, sorted.pop(index+1))
    result = (sorted.index([[2]])+1) * (sorted.index([[6]])+1)
    print(result)


partTwo()