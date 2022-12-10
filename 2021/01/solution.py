file = open("input.txt", "r")

input_raw = file.readlines()

input = [int(x.strip("/n")) for x in input_raw]


def partOne():
    counter = 0
    for element_index in range(len(input)):
        if element_index == 0:
            pass
        elif input[element_index] > input[element_index-1]:
            counter += 1
    print(counter)

def sumThree(index):
    return input[index] + input[index+1] + input[index+2]

def partTwo():
    counter = 0
    
    for element_index in range(len(input)-2):
        if element_index == 0:
            pass
        else:
            if sumThree(element_index) > sumThree(element_index-1):
                counter += 1
    print(counter)


partOne()
partTwo()