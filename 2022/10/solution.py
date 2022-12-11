with open("2022/Day10/input.txt") as inputFile:
    input = inputFile.read().splitlines()


def one():
    solution = 0
    current_cycle = 0
    register_X = 1
    check_cycles = [20, 60, 100, 140, 180, 220]
    cycles_needed = {"addx": 2, "noop": 1}
    for line in input:
        command = line.split()[0]
        for cycle in range(cycles_needed[command]):
            current_cycle += 1
            if current_cycle in check_cycles:
                    solution += current_cycle*register_X
            if command == "addx" and cycle == range(cycles_needed[command])[-1]:
                register_X += int(line.split()[1])
    print(solution)



def two():
    screen = [["" for col in range(40)] for row in range(6)]
    current_cycle = 0
    register_X = 1
    cycles_needed = {"addx": 2, "noop": 1}
    for line in input:
        command = line.split()[0]
        for cycle in range(cycles_needed[command]):
            current_cycle += 1
            current_row = (current_cycle-1) // 40
            current_pos = (current_cycle-1) % 40
            if abs(register_X-current_pos) <= 1:
                screen[current_row][current_pos] = "#"
            else:
                screen[current_row][current_pos] = "."
            if command == "addx" and cycle == range(cycles_needed[command])[-1]:
                register_X += int(line.split()[1])
    for row in screen:
        print(" ".join(row))

one()
two()
