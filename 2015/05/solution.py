with open("2015/Day5/input.txt") as inputFile:
    input = inputFile.read().splitlines()


def partOne():
    vowels = ["a", "e", "i", "o", "u"]
    forbidden_strings = ["ab", "cd", "pq", "xy"]
    nice_strings = 0

    for string in input:
        double_chars = False
        forbidden = False
        current_vowels = [char for char in string if char in vowels]
        
        for char_index in range(len(string)-1):
            if string[char_index] == string[char_index+1]:
                double_chars = True
            if str(string[char_index]+string[char_index+1]) in forbidden_strings:
                forbidden = True
        
        if len(current_vowels) >= 3 and double_chars and not forbidden:
            nice_strings += 1
    
    print(nice_strings)


def partTwo():
    nice_strings = 0

    for string in input:
        pairs = []
        double_pair = False
        sandwich = False

        # Checking for double pairs
        for char_index in range(len(string)-3):
            sub = string[char_index: char_index+2]
            if sub in string[char_index+2:]:
                double_pair = True

        # Checking for a sandwich
        for char_index in range(len(string)-2):
            if string[char_index] == string[char_index+2]:
                sandwich = True

        if double_pair and sandwich:
            nice_strings += 1
    
    print(nice_strings)


partOne()
partTwo()