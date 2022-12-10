file = open("input.txt", "r")

input_raw = file.readlines()
input = [x.strip("\n") for x in input_raw]


def partOne(input):
    
    possible_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    possible_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    possible_hcl = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    entries = [[]]
    entry_counter = 0
    valid = 0
    for line_index in range(len(input_raw)):
        if input[line_index] == "":
            entry_counter += 1
            entries.append([])
        else:
            line_split = input[line_index].split(" ")
            for item in line_split:
                entries[entry_counter].append(item)
    
    for passport in entries:
        fields = 0
        for field in passport:
            field_split = field.split(":")
            if field_split[0] in possible_fields:
                if field_split[0] == "byr":
                    if field_split[1].isnumeric():
                        if 1920 <= int(field_split[1]) <= 2002:
                            fields += 1
                elif field_split[0] == "iyr":
                    if field_split[1].isnumeric():
                        if 2010 <= int(field_split[1]) <= 2020:
                            fields += 1
                elif field_split[0] == "eyr":
                    if field_split[1].isnumeric():
                        if 2020 <= int(field_split[1]) <= 2030:
                            fields += 1
                elif field_split[0] == "hgt":
                    if field_split[1][-1] == "m" and field_split[1][-2] == "c":
                        height = field_split[1].rstrip("cm")
                        if height.isnumeric():
                            if 150 <= int(height) <= 193:
                                fields += 1
                    elif field_split[1][-1] == "n" and field_split[1][-2] == "i":
                        height = field_split[1].rstrip("in")
                        if height.isnumeric():
                            if 59 <= int(height) <= 76:
                                fields += 1
                elif field_split[0] == "hcl":
                    if field_split[1].startswith("#"):
                        color = field_split[1].lstrip("#")
                        if len(color) == 6:
                            for char in color:
                                if char not in possible_hcl:
                                    break
                            else:
                                fields += 1
                elif field_split[0] == "ecl":
                    if field_split[1] in possible_ecl:
                        fields += 1
                elif field_split[0] == "pid":
                    if len(field_split[1]) == 9:
                        if field_split[1].isnumeric():
                            fields += 1
        
        if fields == 7:
            valid += 1
    print(valid)



partOne(input)
