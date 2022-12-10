file = open("input.txt", "r")

input = file.readlines()

def partOne(input):
    valid_passwords = 0
    for entry in input:
        counter = 0
        password_split = entry.split()
        password = password_split[2]

        for char in password:
            if char == password_split[1][0]:
                counter += 1
        
        ranges = password_split[0].split("-")
        bottom = int(ranges[0])
        top = int(ranges[1])
        
        if bottom <= counter <= top:
            valid_passwords += 1


    print(valid_passwords)

def partTwo(input):
    valid_passwords = 0
    for entry in input:
        password_split = entry.split()
        password = password_split[2]
        
        ranges = password_split[0].split("-")
        bottom = int(ranges[0])
        top = int(ranges[1])
        
        if password[bottom-1] == password_split[1][0] and password[top-1] == password_split[1][0]:
            pass
        elif password[bottom-1] == password_split[1][0] or password[top-1] == password_split[1][0]:
            valid_passwords += 1


    print(valid_passwords)


partOne(input)
partTwo(input)
