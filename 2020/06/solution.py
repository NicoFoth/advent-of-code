file = open("input.txt", "r")

input_raw = file.readlines()
input = [x.strip("\n") for x in input_raw]


def partOne(input):
    answers = [[]]
    answer_counter = 0
    total_yes = 0

    for line_index in range(len(input)):
        if input[line_index] == "":
            answer_counter += 1
            answers.append([])
        else:
            answers[answer_counter].append(input[line_index])
    print(answers)

    for group in answers:
        yes = []
        for person in group:
            for char in person:
                if char in yes:
                    pass
                else:
                    yes.append(char)
        
        total_yes += len(yes)

    print(total_yes)


def partTwo(input):
    answers = [[]]
    answer_counter = 0
    total_yes = 0

    for line_index in range(len(input)):
        if input[line_index] == "":
            answer_counter += 1
            answers.append([])
        else:
            answers[answer_counter].append(input[line_index])

    for group in answers:
        yes = []
        for person in group:
            for char in person:
                for person2 in group:
                    if char not in person2:
                        break
                else:
                    if char not in yes:
                        yes.append(char)
        total_yes += len(yes)
    print(total_yes)

partOne(input)
partTwo(input)