with open("2022/Day25/input.txt") as inputFile:
    input = inputFile.read().splitlines()

SNAFU_TO_DECIMAL = {"1": 1, "2": 2, "0": 0, "-": -1, "=": -2}

def convertToDecimal(snafu):
    conversion = 0
    for char, index in zip(snafu, range(len(snafu))):
        conversion += SNAFU_TO_DECIMAL[char]*(5**(len(snafu)-index-1))
    return conversion


def convertToSNAFU(decimal):
    character_amount = 0
    while True:
        character_amount += 1
        if sum([max(SNAFU_TO_DECIMAL.values())*5**i for i in range(character_amount)]) >= decimal:
            break

    snafu = "0" * character_amount
    for i in range(character_amount):
        snafu = min(
            [snafu[0:i] + x + snafu[i + 1 :] for x in SNAFU_TO_DECIMAL.keys()],
            key=lambda snafu_temp: abs(decimal - convertToDecimal(snafu_temp))
        )
    assert convertToDecimal(snafu) == decimal
    return snafu


def partOne():
    fuel_amount = 0
    for number in input:
        fuel_amount += convertToDecimal(number)
    
    print(convertToSNAFU(fuel_amount))


partOne()