with open("2021/Day3/input.txt") as inputFile:
    input = inputFile.read().splitlines()


def partOne():

    gamma = "".join(["0" if len([number[i] for number in input if number[i] == "0"]) > len([number[i] for number in input if number[i] == "1"]) else "1" for i in range(12)])
    epsilon = "".join(["1" if len([number[i] for number in input if number[i] == "0"]) > len([number[i] for number in input if number[i] == "1"]) else "0" for i in range(12)])
    print(int(gamma, 2)*int(epsilon, 2))


def PartTwo():
    oxygen_list = input.copy()
    scrubber_list = input.copy()

    current_bit = 0
    while len(oxygen_list) > 1:
        common = ""
        if len([number[current_bit] for number in oxygen_list if number[current_bit] == "0"]) > len([number[current_bit] for number in oxygen_list if number[current_bit] == "1"]):
            common = "0"
        elif len([number[current_bit] for number in oxygen_list if number[current_bit] == "0"]) == len([number[current_bit] for number in oxygen_list if number[current_bit] == "1"]):
            common = "1"
        else:
            common = "1"
        oxygen_list = [x for x in oxygen_list if x[current_bit] == common]
        current_bit += 1

    current_bit = 0
    while len(scrubber_list) > 1:
        common = ""
        if len([number[current_bit] for number in scrubber_list if number[current_bit] == "0"]) < len([number[current_bit] for number in scrubber_list if number[current_bit] == "1"]):
            common = "0"
        elif len([number[current_bit] for number in scrubber_list if number[current_bit] == "0"]) == len([number[current_bit] for number in scrubber_list if number[current_bit] == "1"]):
            common = "0"
        else:
            common = "1"
        scrubber_list = [x for x in scrubber_list if x[current_bit] == common]
        current_bit += 1
    
    print(int(oxygen_list[0], 2)*int(scrubber_list[0], 2))


partOne()
PartTwo()