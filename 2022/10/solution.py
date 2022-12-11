with open("2022/Day10/input.txt") as inputFile:
    input = inputFile.read().splitlines()


def one():
    solution = 0
    current_cycle = 0
    register_X = 1
    check_cycles = [20, 60, 100, 140, 180, 220]
    signal_strengs = []
    for line in input:
        command = line.split()[0]
        if command == "addx":
            for cycle in range(2):
                current_cycle += 1
                if current_cycle in check_cycles:
                    solution += current_cycle*register_X
                if cycle == 1:
                    register_X += int(line.split()[1])
        elif command == "noop":
            current_cycle += 1
            if current_cycle in check_cycles:
                    solution += current_cycle*register_X

    print(solution)



def two():
    screen = [["" for col in range(40)] for row in range(6)]
    current_cycle = 0
    register_X = 1
    for line in input:
        command = line.split()[0]
        if command == "addx":
            for cycle in range(2):
                current_cycle += 1

                current_row = (current_cycle-1) // 40
                current_pos = (current_cycle-1) % 40
                if abs(register_X-current_pos) <= 1:
                    screen[current_row][current_pos] = "#"
                else:
                    screen[current_row][current_pos] = "."

                if cycle == 1:
                    register_X += int(line.split()[1])
        elif command == "noop":
            current_cycle += 1
            current_row = (current_cycle-1) // 40
            current_pos = (current_cycle-1) % 40
            if abs(register_X-current_pos) <= 1:
                screen[current_row][current_pos] = "#"
            else:
                screen[current_row][current_pos] = "."

    for row in screen:
        print(" ".join(row))

one()
two()
