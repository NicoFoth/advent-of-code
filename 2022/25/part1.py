with open("2022/Day25/input.txt") as inputFile:
    input = inputFile.read().splitlines()


def partOne():
    fuel_amount = 0
    for number in input:
        conversion = 0
        for char, index in zip(number, range(len(number))):
            if char == "2" or char == "1":
                conversion += int(char)*(5**(len(number)-index-1))
            elif char == "-":
                conversion -= (5**(len(number)-index-1))
            elif char == "=":
                conversion -= 2*(5**(len(number)-index-1))
        fuel_amount += conversion
    
    # Convert fuel_amount to SNAFU

partOne()