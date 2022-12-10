input_file = open("input.txt" , "r")

input_list_raw = input_file.readlines()

input_file.close()

input_list = [int(x.strip("\n")) for x in input_list_raw]


def partOne(input_list):
    for i in range(len(input_list)):

        for j in range(len(input_list)):

            if i == j: 
                break
            elif input_list[i] + input_list[j] == 2020:
                solution = input_list[i] * input_list[j]

                print(solution)



def partTwo(input_list):
    for i in range(len(input_list)):

        for j in range(len(input_list)):

            for k in range(len(input_list)):

                if i == j or j == k or i == k:
                    break

                elif input_list[i] + input_list[j] + input_list[k] == 2020:
                    solution = input_list[i] * input_list[j] * input_list[k]

                    print(solution)


partOne(input_list)
partTwo(input_list)