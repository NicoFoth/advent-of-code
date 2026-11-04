import hashlib

input = open("input.txt").read().strip()

def partOne():
    i = 0
    hex_result = ""
    while not hex_result.startswith("00000"):
        i += 1
        hex_result = hashlib.md5((input+str(i)).encode()).hexdigest()
    print(i)


def partTwo():
    i = 0
    hex_result = ""
    while not hex_result.startswith("000000"):
        i += 1
        hex_result = hashlib.md5((input+str(i)).encode()).hexdigest()
    print(i)


partOne()
partTwo()