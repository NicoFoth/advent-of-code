with open("input.txt") as inputFile:
        input = inputFile.readlines()

def one():
    total_calories = []
    current_calories = 0
    for line in input:
        if line == "\n":
            total_calories.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(line)
    total_calories.sort(reverse=True)
    print(total_calories[0])


def two():
    total_calories = []
    current_calories = 0
    for line in input:
        if line == "\n":
            total_calories.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(line)
    total_calories.sort(reverse=True)
    print(total_calories[0]+total_calories[1]+total_calories[2])


one()
two()