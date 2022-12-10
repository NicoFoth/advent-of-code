file = open("input.txt")

input_raw = file.readlines()
input = [x.strip(".\n") for x in input_raw]

def partOne(input):
    global_command_index = 0
    previous_commands = []
    accumulator = 0
    for _ in range(len(input)):
        command_type = input[global_command_index].split(" ")[0]
        command_value = int(input[global_command_index].split(" ")[1])

        if global_command_index not in previous_commands:
            if command_type == "nop":
                previous_commands.append(global_command_index)
                global_command_index += 1
            elif command_type == "acc":
                previous_commands.append(global_command_index)
                accumulator += command_value
                global_command_index += 1
            elif command_type == "jmp":
                previous_commands.append(global_command_index)
                global_command_index += command_value
        else:
            print(accumulator)
            break


def partTwoSub(input, notToChange):
    global_command_index = 0
    previous_commands = []
    accumulator = 0
    changed = False
    while True:
        command_type = input[global_command_index].split(" ")[0]
        command_value = int(input[global_command_index].split(" ")[1])

        print(command_value, global_command_index <= len(input)-1)
        if global_command_index <= len(input)-1:
            if global_command_index not in previous_commands:
                if command_type == "nop":
                    previous_commands.append(global_command_index)
                    global_command_index += 1
                elif command_type == "acc":
                    previous_commands.append(global_command_index)
                    accumulator += command_value
                    global_command_index += 1
                elif command_type == "jmp":
                    if global_command_index + command_value in previous_commands:
                        if changed == True:
                            return False, global_command_index
                        if global_command_index not in notToChange:
                            input[global_command_index] = f"nop {command_value}"
                            previous_commands.append(global_command_index)
                            global_command_index += 1
                            changed = True
                    else:
                        previous_commands.append(global_command_index)
                        global_command_index += command_value
        else:
            return True, accumulator

def partTwo(input):
    notToChange = []
    acc = 0
    loop = False
    while loop == False:
        result = partTwoSub(input, notToChange)
        if result[0] == False:
            notToChange.append(result[1])
    
        elif result[0] == True:
            loop = True
            acc += result[1]

    print(acc)
        


partOne(input)
partTwo(input)