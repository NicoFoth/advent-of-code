with open("input.txt") as inputFile:
    input = inputFile.readlines()

def one():
    count = 0
    for pair in input:
        elf1 = pair.split(",")[0]
        elf2 = pair.split(",")[1]
        range1 = range(int(elf1.split("-")[0]), int(elf1.split("-")[1])+1)
        range2 = range(int(elf2.split("-")[0]), int(elf2.split("-")[1])+1)
        
        if set(range1).issubset(range2):
            count += 1
        elif set(range2).issubset(range1):
            count += 1
    print(count)


def two():
    count = 0
    for pair in input:
        elf1 = pair.split(",")[0]
        elf2 = pair.split(",")[1]
        range1 = range(int(elf1.split("-")[0]), int(elf1.split("-")[1])+1)
        range2 = range(int(elf2.split("-")[0]), int(elf2.split("-")[1])+1)

        for i in range1:
            if i in range2:
                count += 1
                break
    print(count)

one()
two()