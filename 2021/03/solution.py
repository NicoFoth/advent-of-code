file = open("input.txt", "r")

input_raw = file.readlines()

input = [x.strip("\n") for x in input_raw]

def partOne(input):
    common = []
    uncommon = []
    for i in range(12):
        counter0 = 0
        counter1 = 0

        for number in input:
            if number[i] == "1":
                counter1 += 1
            elif number[i] == "0":
                counter0 += 1
        if counter0 > counter1:
            common.append("0")
            uncommon.append("1")
        else:
            common.append("1")
            uncommon.append("0")
    
    common_str = "".join(common)
    uncommon_str = "".join(uncommon)
    print(int(common_str, 2)*int(uncommon_str, 2))


def popWithNumber(list, string, index):
    toDelete = []
    for item_index in range(len(list)):
        if list[item_index][index] != string:
            toDelete.append(list[item_index])
    for i in toDelete:
        list.remove(i)
    return list



def partTwo(input):

    safe_input = input.copy()

    common = input
    while len(common) > 1:

        for i in range(12):
            counter0 = 0
            counter1 = 0
            for number in input:
                if number[i] == "1":
                    counter1 += 1
                elif number[i] == "0":
                    counter0 += 1
            if counter0 > counter1:
                common = popWithNumber(common, "0", i)
            else:
                common = popWithNumber(common, "1", i)
    print(common)

    uncommon = safe_input

    while len(uncommon) > 1:

        for i in range(12):
            if len(uncommon) == 1:
                break
            counter0 = 0
            counter1 = 0
            for number in safe_input:
                if number[i] == "1":
                    counter1 += 1
                elif number[i] == "0":
                    counter0 += 1
            if counter0 < counter1:
                uncommon = popWithNumber(uncommon, "0", i)
            else:
                uncommon = popWithNumber(uncommon, "1", i)
    print(uncommon)

    print(int(common[0], 2)*int(uncommon[0], 2))




partTwo(input)