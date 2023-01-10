with open("2022/Day13/input.txt") as inputFile:
    input = inputFile.read().splitlines()

    pairs = [[eval(input[line_index-2]), eval(input[line_index-1])] for line_index in range(len(input)) if input[line_index] == ""]


def eval_list(list1, list2):
    ordered = True
    for element0, element1 in zip(list1, list2):
            if type(element0) == type(element1):
                if type(element0) == list:
                    if not eval_list(element0, element1):
                        ordered = False
                        break
                    else:
                        break
                elif element0 < element1:
                    break
                elif element0 > element1:
                    ordered = False
                    break
            else:
                if type(element0) == list:
                    element1 = [element1]
                else:
                    element0 = [element0]
                if not eval_list(element0, element1):
                    ordered = False
                    break
                else:
                    break
    else:
        if len(list1) > len(list2):
            ordered = False
    return ordered


def partOne():
    indices_sum = 0
    for pair, index in zip(pairs, range(1, len(pairs)+1)):
        if eval_list(pair[0], pair[1]):
            indices_sum += index
    print(indices_sum)

partOne()