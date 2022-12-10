with open("input.txt") as inputFile:
        input = inputFile.readlines()

def one():
    score = 0
    for rucksack in input:
        compartment1 = set(rucksack[:len(rucksack)//2])
        compartment2 = set(rucksack[len(rucksack)//2:])
        score += itemValues(next(iter((compartment1 & compartment2))))
    print(score)

def two():
    score = 0
    for i in range(0, len(input), 3):
        badge = set.intersection(set(input[i].strip("\n")), set(input[i+1].strip("\n")), set(input[i+2].strip("\n")))
        score += itemValues(next(iter(badge)))
    print(score)

def itemValues(char):
    ascii_value = ord(char)
    if ascii_value > 96:
        return ascii_value - 96
    else:
        return ascii_value - 64 + 26


one()
two()